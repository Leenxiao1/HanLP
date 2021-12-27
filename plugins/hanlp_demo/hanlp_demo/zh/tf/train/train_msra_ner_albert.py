# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-12-28 23:15
from hanlp.components.ner_tf import TransformerNamedEntityRecognizerTF
from hanlp.datasets.ner.msra import MSRA_NER_CHAR_LEVEL_TRAIN, MSRA_NER_CHAR_LEVEL_DEV, MSRA_NER_CHAR_LEVEL_TEST
from tests import cdroot

cdroot()
recognizer = TransformerNamedEntityRecognizerTF()
save_dir = 'data/model/ner/msra_ner_albert_base'
recognizer.fit(MSRA_NER_CHAR_LEVEL_TRAIN, MSRA_NER_CHAR_LEVEL_DEV, save_dir,
               transformer='uer/albert-base-chinese-cluecorpussmall',
               learning_rate=5e-5,
               metrics='accuracy')  # Use accuracy to speed up training
recognizer.load(save_dir, metrics='f1')
print(recognizer.predict(list('上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。')))
recognizer.evaluate(MSRA_NER_CHAR_LEVEL_TEST, save_dir=save_dir)
print(f'Model saved in {save_dir}')
