from database.common import get_from_db


def get_random_dinner_ideas(meal_count):
    sql = 'SELECT m."name", c."name" FROM dinner_ideas.meals m left join dinner_ideas.categories c on m.category_id = c.id ORDER BY RANDOM() LIMIT %s'
    args = (meal_count,)
    dinner_rows = get_from_db(sql, args)
    meals = []

    for row in dinner_rows:
        meals.append({"name":row[0], "category":row[1]})

    return meals
