provider "azurerm" {
  features {}
}

resource "azurerm_sentinel_data_connector_azure_active_directory" "entra" {
  name                       = "entra-signin"
  log_analytics_workspace_id = var.workspace_id
}

variable "workspace_id" {
  type = string
}
