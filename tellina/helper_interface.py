"""
Interface to the neural translation model.
"""
import tensorflow as tf

import os
import sys

commandline_helper_dir = os.path.join(os.path.dirname(__file__), "..", "tellina_learning_module")
sys.path.append(commandline_helper_dir)

from encoder_decoder import classifiers
from encoder_decoder import data_utils
from encoder_decoder import decode_tools
from encoder_decoder import translate as trans

os.environ["CUDA_VISIBLE_DEVICES"] = "2"

FLAGS = tf.app.flags.FLAGS

FLAGS.demo = True
FLAGS.fill_argument_slots = True

FLAGS.normalized = True
FLAGS.encoder_topology = 'birnn'

FLAGS.dim = 400
FLAGS.batch_size = 16
FLAGS.num_layers = 1
FLAGS.learning_rate = 0.0001
FLAGS.encoder_input_keep = 0.5
FLAGS.encoder_output_keep = 0.5
FLAGS.decoder_input_keep = 0.5
FLAGS.decoder_output_keep = 0.5

FLAGS.use_attention = True
FLAGS.attention_input_keep = 0.5
FLAGS.attention_output_keep = 0.5
FLAGS.beta = 0.0

FLAGS.decoding_algorithm = 'beam_search'
FLAGS.beam_size = 100
FLAGS.alpha = 1.0

FLAGS.nl_vocab_size = 1000
FLAGS.cm_vocab_size = 1000

FLAGS.data_dir = os.path.join(commandline_helper_dir, "data", "bash")
FLAGS.model_dir = os.path.join(commandline_helper_dir, "model", "seq2seq")

if FLAGS.fill_argument_slots:
    # create slot filling classifier
    model_param_dir = os.path.join(FLAGS.data_dir, 'train.{}.mappings.X.Y'
                           .format(FLAGS.sc_vocab_size))
    train_X, train_Y = data_utils.load_slot_filling_data(model_param_dir)
    slot_filling_classifier = \
            classifiers.KNearestNeighborModel(1, train_X, train_Y)
    print('Slot filling classifier parameters loaded.')
else:
    slot_filling_classifier = None

# create tensorflow session
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                  log_device_placement=FLAGS.log_device_placement))

# create model and load nerual model parameters.
model, _ = trans.create_model(sess, forward_only=True, buckets=[(30, 40)])
nl_vocab, _, _, rev_cm_vocab = data_utils.load_vocab(FLAGS)

def translate_fun(sentence, slot_filling_classifier=slot_filling_classifier):
    return decode_tools.translate_fun(sentence, sess, model, nl_vocab, rev_cm_vocab, 
                    FLAGS, slot_filling_classifier)
