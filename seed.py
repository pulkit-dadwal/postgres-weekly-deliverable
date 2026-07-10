from random import choice, randint, uniform

from faker import Faker

from app.database import SessionLocal
from app.models.category import Category
from app.models.customer import Customer
from app.models.employee import Employee
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem

fake = Faker()

db = SessionLocal()


def seed_categories():
    print("Seeding Categories...")

    categories = [
        "Coffee",
        "Tea",
        "Cold Coffee",
        "Smoothies",
        "Desserts",
        "Pastries",
        "Sandwiches",
        "Snacks",
    ]

    objects = [Category(name=name) for name in categories]

    db.bulk_save_objects(objects)
    db.commit()


def seed_employees():
    print("Seeding Employees...")

    roles = ["Manager", "Barista", "Cashier"]

    employees = [
        Employee(
            name=fake.name(),
            role=choice(roles),
        )
        for _ in range(20)
    ]

    db.bulk_save_objects(employees)
    db.commit()


def seed_customers():
    print("Seeding Customers...")

    customers = [
        Customer(
            name=fake.name(),
            email=fake.unique.email(),
            phone=fake.msisdn()[:10],
        )
        for _ in range(5000)
    ]

    db.bulk_save_objects(customers)
    db.commit()


def seed_products():
    print("Seeding Products...")

    category_ids = [c.id for c in db.query(Category).all()]

    products = [
        Product(
            name=f"{fake.word().capitalize()} Coffee",
            price=round(uniform(80, 350), 2),
            category_id=choice(category_ids),
        )
        for _ in range(100)
    ]

    db.bulk_save_objects(products)
    db.commit()


def seed_orders():
    print("Seeding Orders...")

    customer_ids = [c.id for c in db.query(Customer).all()]
    employee_ids = [e.id for e in db.query(Employee).all()]

    statuses = [
        "Pending",
        "Preparing",
        "Completed",
        "Cancelled",
    ]

    orders = [
        Order(
            customer_id=choice(customer_ids),
            employee_id=choice(employee_ids),
            total_amount=round(uniform(100, 1200), 2),
            status=choice(statuses),
            order_time=fake.date_time_between(
                start_date="-1y",
                end_date="now",
            ),
        )
        for _ in range(20000)
    ]

    db.bulk_save_objects(orders)
    db.commit()


def seed_order_items():
    print("Seeding Order Items...")

    order_ids = [o.id for o in db.query(Order).all()]
    product_ids = [p.id for p in db.query(Product).all()]

    order_items = [
        OrderItem(
            order_id=choice(order_ids),
            product_id=choice(product_ids),
            quantity=randint(1, 5),
        )
        for _ in range(60000)
    ]

    db.bulk_save_objects(order_items)
    db.commit()


def main():
    print("=" * 50)
    print("Coffee Shop Database Seeding")
    print("=" * 50)

    seed_categories()
    seed_employees()
    seed_customers()
    seed_products()
    seed_orders()
    seed_order_items()

    db.close()

    print("=" * 50)
    print("Database seeded successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()