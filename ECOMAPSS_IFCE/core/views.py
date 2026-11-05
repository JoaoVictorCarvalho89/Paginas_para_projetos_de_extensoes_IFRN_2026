# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages

""" Imports de São Jorge Suplementos """

from .models import Produto, Fornecedor, Cliente #Classes de modelos
from .forms import ProdutoForm, FornecedorForm, ClienteForm #Classes de formulários
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import logging

logger = logging.getLogger('django.template')
logger.debug("Teste: sistema de log está funcionando!")

""" PÁGINAS PRINCIPAIS"""

def index(request):
    return render(request, 'index.html')
