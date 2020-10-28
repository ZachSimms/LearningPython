from ecommerce import sales
from ecommerce.shopping import employees
import sys

#print(sys.path)
sales.calc_shipping()
sales.calc_tax()
employees.employee_pay()
employees.employee_interview()