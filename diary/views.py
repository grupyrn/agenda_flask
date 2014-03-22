# -*- coding: utf-8 -*-

from flask import Blueprint, render_template


diary = Blueprint('diary', __name__)


@diary.route('/')
def index():
    return render_template('index.html')
