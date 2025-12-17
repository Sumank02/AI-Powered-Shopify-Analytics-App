SALES_OVERVIEW_QUERY = """
FROM orders
SHOW
  sum(line_items.quantity) AS total_quantity,
  sum(total_price) AS total_sales
GROUP BY line_items.product_title
SINCE {start_date}
UNTIL {end_date}
ORDER BY total_quantity DESC
LIMIT {limit}
"""

INVENTORY_LEVELS_QUERY = """
FROM inventory_levels
SHOW
  sum(available) AS available_quantity
GROUP BY product_title
"""

REPEAT_CUSTOMERS_QUERY = """
FROM orders
SHOW
  count(order_id) AS order_count
GROUP BY customer_id
HAVING order_count > 1
SINCE {start_date}
UNTIL {end_date}
"""
