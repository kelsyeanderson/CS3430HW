#!/usr/bin/python

import os
import argparse
import cv2
import sys
import random
import numpy as np
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier

#################################################
# module: dtr_rf.py
# Kelsye Anderson
# A02093326
##################################################

## ================== LOADING DATA =======================

## Change the value of BEE_DIR accordingly
BEE = []
BEE_DIR = '/Desktop/Homework/CS3430HW/Exam3'
TARGET = []
DATA = []

def generate_file_names(fnpat, rootdir):
  # your code
  for path, subdir, filelist in os.walk(rootdir):
      for name in filelist:
          if not name.startswith('.') and not re.match(fnpat, name) is None:
              yield os.path.join(path, name)
          for dir in subdir:
              generate_file_names(fnpat, dir)

def load_data(imgdir):
  ## your code
  bin_size = 8
  for imgp in generate_file_names(r'.+\.(jpg|png|JPG)', imgdir):
    print('indexing ' + imgp)
    img = cv2.open(imgp)
    input = cv2.calcHist([img], [0, 1, 2], None, [bin_size, bin_size, bin_size], [0, 256, 0, 256, 0, 256])
    norm_hist = cv2.normalize(input, input).flatten()
    HIST_INDEX[imgp] = norm_hist
    print(imgp + ' indexed')
  pass

## ===================== DECISION TREES ==============================

def run_dtr_train_test_split(data, target, n, test_size):
  ## your code
  pass

def plot_dtr_train_test_split(acc_pred_list, n, test_size):
  ## your code
  pass

def run_dtr_cross_validation(data, target, test_size):
  ## your code
  pass

def plot_dtr_cross_validation(nf_acc_list, nf_lower, nf_upper, test_size):
  ## your code
  pass

def compute_cr_cm(data, target, test_size):
  ## your code
  pass

## ================= RANDOM FORESTS ==============================
    
def create_rfs(n, num_trees, data, target):
  ## your code
  pass

def classify_with_rfs_aux(rand_forests, data_item):
  ## your code
  pass

def classify_with_rfs(rfs, data, target):
  ## your code
  pass

def run_rf_mv_experiments(rfs, data, target, n):
  ## your code
  pass

def collect_rf_mv_stats(rfs_list, data, target, n):
  num_trees_acc_list = []
  for num_trees, rfs in rfs_list:
    num_trees_acc_list.append((num_trees,
                               run_rf_mv_experiments(rfs,
                                                     data,
                                                     target,
                                                     n)))
  return num_trees_acc_list

def create_rf_list(ntrees_in_rf, data, target):
  ## your code
  pass

def plot_rf_mv_stats(rf_mv_stats, num_trees_lower, num_trees_upper):
  ## your code
  pass
  

    

