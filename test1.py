from CheffAssistant import Inventory
from analytics import get_usage_analytics

inventory = Inventory()
analytics = get_usage_analytics(inventory.usage_history, inventory.ingredients)

for ing, data in analytics.items():
    print(f"{ing}: {data}")
