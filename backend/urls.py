from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from backend.app.adapters import integration
from backend.app.adapters import rule_engine

admin.site.site_header = "Smart Rule Engine Admin Panel"
admin.site.site_title = "Smart Rule Engine Admin Panel"
admin.site.index_title = "Smart Rule Engine Admin Panel"


schema_view = get_schema_view(
   openapi.Info(
      title="Smart Rule Engine REST API",
      default_version='v1.0.0',
      description="Smart Rule Engine REST API",
   ),
)


urlpatterns = [
    path(r'admin/', admin.site.urls, name="admin"),
    path(r'docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='docs'
    ),
    path(
        'api/v1/integration/',
        integration.IntegrationListView.as_view(),
        name='tenant_list'
    ),
    path(
        'api/v1/integration/<int:pk>/',
        integration.IntegrationDetailView.as_view(),
        name='tenant_detail'
    ),
    path(
        'api/v1/rule-chain/',
        rule_engine.RuleChainListView.as_view(),
        name='rule_chain_list'
    ),
    path(
        'api/v1/rule-chain/<int:pk>/',
        rule_engine.RuleChainDetailView.as_view(),
        name='rule_chain_detail'
    ),
    path(
        'api/v1/rule-chain/generate/',
        rule_engine.GenerateRuleChainView.as_view(),
        name='generate_rulechain'
    ),

]
