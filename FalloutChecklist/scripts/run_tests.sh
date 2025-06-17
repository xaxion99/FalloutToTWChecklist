#!/bin/bash

# Activate virtual environment if needed
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi

# Run Django tests with verbosity=2
cd ..  # Needed to run in PyCharm
# python manage.py test --verbosity=1
python manage.py test --verbosity=2
# python manage.py test --verbosity=3
