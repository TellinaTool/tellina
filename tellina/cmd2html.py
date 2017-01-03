import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"..", "tellina_learning_module"))

from bashlex import data_tools

def cmd2html(cmd_str):
  """ A wrapper for the function ast2html (see below) that takes in a cmd string 
  and translate into a html string with highlinghting.
  """
  root = data_tools.bash_parser(cmd_str)
  return " ".join(ast2html(root))

def ast2html(node):
  """ Translate a bash AST from tellina_learning_module/bashlex/nast.py into html code,
    with proper syntax highlighting.
    Argument:
      node: an ast returned from tellina_learning_module.data_tools.bash_parser(cmd_str)
    Returns:
      a html string that can be embedded into your browser with appropriate syntax highlighting
  """
  html_spans = []

  if node.kind == "root":
    for child in node.children:
      html_spans.extend(ast2html(child))
  elif node.kind == "pipeline":
    is_first = True
    for child in node.children:
      if is_first:
        is_first = False
      else:
        html_spans.append("|")
      html_spans.extend(ast2html(child))
  elif node.kind == "headcommand":
    span = "<span class=\"hljs-built_in\">" + node.value + "</span>"
    html_spans.append(span)
    for child in node.children:
      html_spans.extend(ast2html(child))
  elif node.kind == "flag":
    span = "<span class=\"hljs-keyword\">" + node.value + "</span>"
    html_spans.append(span)
    for child in node.children:
      html_spans.extend(ast2html(child))
  elif node.kind == "argument":
    span = "<span class=\"hljs-semantic_types\">" + node.value + "</span>"
    html_spans.append(span)
    for child in node.children:
      html_spans.extend(ast2html(child))
  elif node.kind == "bracket":
    html_spans.append("\\(")
    for child in node.children:
      html_spans.extend(ast2html(child))
    html_spans.append("\\)")
  elif node.kind in ["binarylogicop", "unarylogicop", "redirect"]:
    span = "<span class=\"hljs-keyword\">" + node.value + "</span>"
    html_spans.append(span)
  elif node.kind in ["commandsubstitution", "processsubstitution"]:
    html_spans.append(node.value)
    html_spans.append("(")
    for child in node.children:
      html_spans.extend(ast2html(child))
    html_spans.append(")")
  else:
    #print node.kind
    html_spans.append(node.value)

  return html_spans

def test():
  cmd_str_list = [
    "find Path -iname Regex -exec grep -i -l Regex {} \;",
    "find Path -type f -iname Regex | xargs -I {} grep -i -l Regex {}",
    "find Path \( -name Regex-01 -or -name Regex-02 \) -print",
    "find Path -not -name Regex",
    "find <(echo \"hello\")",
    "find Documents \( -name \"*.py\" -o -name \"*.html\" \)"
  ];
  for cmd_str in cmd_str_list:
    print(cmd2html(cmd_str)) 

if __name__ == '__main__':
  test()