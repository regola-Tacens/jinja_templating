from jinja2 import Environment, FileSystemLoader
from datetime import datetime

today = datetime.today()
t = today.strftime('%d.%m.%Y %H:%M')

environment = Environment(loader=FileSystemLoader("PM_templates/"))
template = environment.get_template("maps.html")

field1 = {
  "name": "Les Vignes",
  "product": "Wheatseeds",
  "unitPerSurface": "kg/ha",
  "unit": "kg",
  "area": 6.5,
  "comment": "this is a comment",
  "totalUsage": {
    "amount": 1.521,
    "units": {
      "amount": 60.84,
      "name": "doses"
    },
    "conditionning": {
      "name": "bags",
      "amount": 2.53
    }
  },
  "average": {
    "amount": 234,
    "units": {
      "amount": 9.36,
      "name": "doses"
    },
  },
  "footer": {
    "pmg": {
      "amount": 50,
    },
    "units": {
      "amount": 500.000,
      "unit": "grains",
      "name": "doses"
    },
    "conditionning": {
      "amount": 125.000,
      "unit": "grains",
      "name": "big bags"
    }
  }
}

field2 = {
  "name": "Les Vignes",
  "product": "Azote Liquide 33%(33-20-0)",
  "unitPerSurface": "L/ha",
  "unit": "L",
  "area": 6.5,
  "totalUsage": {
    "amount": 120.25,
    "units": {
      "amount": 39.68,
      "name": "units(N)"
    },
    "conditionning": {
      "name": "units(P)",
      "amount": 24.05
    }
  },
  "average": {
    "amount": 8.5,
    "units": {
      "amount": 6.1,
      "name": "units/ha (N)"
    },
    "conditionning": {
      "name": "units/ha (P)",
      "amount": 3.7
    }
  }
}

fields= [field1, field2]

for index, field in enumerate(fields):
  filename = f"./generated/map{index}.html"
  content = template.render(
    {
      "date": t,
      "field": field,
      "page": index
    }
  )
  with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"... wrote (filename")