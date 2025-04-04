from datetime import datetime, timedelta

def get_usage_analytics(usage_history, current_inventory):
    """
    Returns a dictionary with usage data per ingredient including:
    - Weekly usage
    - Estimated weeks remaining
    - Suggested restock amount
    """
    analytics = {}

    for ingredient, history in usage_history.items():
        # Only consider consumption (negative values)
        weekly_usage = [x for x in history if isinstance(x, int) and x < 0]
        total_usage = abs(sum(weekly_usage))  # sum is negative, make it positive

        avg_per_week = total_usage  # For now, assumes this is from 1 week of data

        current_stock = current_inventory.get(ingredient, 0)
        if avg_per_week > 0:
            weeks_remaining = current_stock / avg_per_week
        else:
            weeks_remaining = float("inf")  # No usage, unlimited stock

        restock_suggestion = max(0, int((2 * avg_per_week) - current_stock))

        analytics[ingredient] = {
            "weekly_usage": total_usage,
            "avg_per_week": avg_per_week,
            "current_stock": current_stock,
            "weeks_remaining": round(weeks_remaining, 2),
            "restock_suggestion": restock_suggestion
        }

    return analytics
