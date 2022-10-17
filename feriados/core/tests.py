from http import HTTPStatus
from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase

from core.models import FeriadoModel


class FeriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(resolve_url('feriado'))

    def test_200_response(self):
        self.assertEqual(HTTPStatus.OK, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Feriado')

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')

class TirantesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(resolve_url('tiradentes'))

    def test_200_response(self):
        self.assertEqual(HTTPStatus.OK, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Tiradentes')


class FeriadoModelTest(TestCase):

    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel.objects.create(nome=self.feriado,  dia=self.dia,  mes=self.mes)

    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.feriado)

    def test_dia_feriado(self):
        dia = self.cadastro.__dict__.get('dia', '')
        self.assertEqual(dia, self.dia)
