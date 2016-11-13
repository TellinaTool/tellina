"""
Interface to the neural translation model.
"""
import tensorflow as tf

import os
import sys

commandline_helper_dir = os.path.join(os.path.dirname(__file__), "..", "commandline-helper")
sys.path.append(commandline_helper_dir)

from encoder_decoder import data_utils
from encoder_decoder import decode_tools
from encoder_decoder import translate as trans

FLAGS = tf.app.flags.FLAGS

FLAGS.demo = True
FLAGS.normalized = True

FLAGS.dim = 200
FLAGS.batch_size = 16
FLAGS.num_layers = 1
FLAGS.learning_rate = 0.0001
FLAGS.encoder_input_keep = 0.6
FLAGS.encoder_output_keep = 0.6
FLAGS.decoder_input_keep = 0.6
FLAGS.decoder_output_keep = 0.6

FLAGS.use_attention = True
FLAGS.attention_input_keep = 0.6
FLAGS.attention_output_keep = 0.6
FLAGS.beta = 0.0

FLAGS.decoding_algorithm = 'beam_search'
FLAGS.beam_size = 50
FLAGS.alpha = 1.0

FLAGS.nl_vocab_size = 1000
FLAGS.cm_vocab_size = 1000

FLAGS.data_dir = os.path.join(commandline_helper_dir, "data", "bash")
FLAGS.model_dir = os.path.join(commandline_helper_dir, "model", "seq2seq")

# create tensorflow session
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                  log_device_placement=FLAGS.log_device_placement))

# create model and load parameters.
model, _ = trans.create_model(sess, forward_only=True, buckets=[(20, 50)])
nl_vocab, _, _, rev_cm_vocab = data_utils.load_vocab(FLAGS)

def translate_fun(sentence):
    return decode_tools.translate_fun(sentence, sess, model, nl_vocab, rev_cm_vocab, FLAGS)
