"""
Interface to the neural translation model.
"""
import tensorflow as tf

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "commandline-helper"))

import encoder_decoder.data_utils as data_utils
import encoder_decoder.decode_tools as decode_tools
import encoder_decoder.parse_args as parse_args
import encoder_decoder.translate as trans

FLAGS = tf.app.flags.FLAGS

parse_args.define_input_flags()

# create tensorflow session
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                  log_device_placement=FLAGS.log_device_placement))

# create buckets
if FLAGS.decoder_topology in ['basic_tree']:
    _buckets = [(5, 30), (10, 30), (20, 40), (30, 64), (40, 64)]
elif FLAGS.decoder_topology in ['rnn']:
    _buckets = [(5, 20), (10, 20), (20, 30), (30, 40), (40, 40)]

# create model and load parameters.
model, _ = trans.create_model(sess, forward_only=True)
nl_vocab, _, _, rev_cm_vocab = data_utils.load_vocab(FLAGS)

def translate_fun(sentence):
    return decode_tools.translate_fun(sentence, sess, model, nl_vocab, rev_cm_vocab, FLAGS)