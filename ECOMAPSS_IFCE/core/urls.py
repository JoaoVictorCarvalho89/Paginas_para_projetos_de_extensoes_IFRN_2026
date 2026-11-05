from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include 

from .views import index, base, perfil, SobreNos, tela_whatsapp, carrinho, PaginaCliente, teste #Páginas principais
from .views import forms, autenticacao, desconectar, recuperar_senha, dashboard, forms_base #Formulários 
from .views import produto_cadastro, produto_editar, produto_remover #Crud de Produtos
from .views import fornecedores, fornecedor_cadastro, fornecedor_editar, fornecedor_remover, lista_clientes, cliente_editar, cliente_remover #Crud de Fornecedores
from .views import cabecalho, footer, main, barra_lateral #Elementos de Layout

urlpatterns = [

    path('admin/', admin.site.urls),

    # Páginas Principais

    path('base/', base, name='base'),
    path('', index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)