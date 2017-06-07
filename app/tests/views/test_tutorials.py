# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from app.tests.mixins import RouteTestingWithKwargs

import app.views as views

import pep8

tutorials = views.tutorials_views


class TutorialsPep8Tests(TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        path = 'app/views/tutorials/'
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([path + 'views.py',
                                        path + 'urls.py',
                                        path + '__init__.py'])
        error_message = ""
        if result.total_errors != 0:
            error_message = "Style errors in: " + path + "\n" + "\n".join(result.get_statistics())
        self.assertEqual(result.total_errors, 0, error_message)


class TutorialTestsIndex(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_index'
        self.route = '/tutorial'
        self.view = tutorials.index
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 200,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


class TutorialsCredentialsTests(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_credentials'
        self.route = '/tutorials/credentials'
        self.view = tutorials.credentials
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


class TutorialsIdTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_id'
        self.route = '/tutorials/100'
        self.view = tutorials.id
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 200,
            'PATCH': 200,
            'DELETE': 200,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'id_number': 22}


class TutorialsIdEditsTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_id_edit'
        self.route = '/tutorials/100/edit'
        self.view = tutorials.id_edit
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'id_number': 22}


class TutorialsNewTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_new'
        self.route = '/tutorials/new'
        self.view = tutorials.new
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}
