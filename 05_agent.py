from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


# Mock business data
orders = {
    "1001": {
        "status": "delivered",
        "amount": 150.00,
        "refundable": False,
    },
    "1002": {
        "status": "delayed",
        "amount": 220.00,
        "refundable": True,
    },
    "1003": {
        "status": "being prepared",
        "amount": 80.00,
        "refundable": True,
    },
}


@tool
def get_order_status(order_id: str) -> str:
    """Get the current status of a customer order using its order ID."""

    order = orders.get(order_id)

    if order is None:
        return f"Order {order_id} was not found."

    return (
        f"Order ID: {order_id}; "
        f"status: {order['status']}."
    )


@tool
def calculate_refund(order_id: str) -> str:
    """Calculate the available refund amount for an order."""

    order = orders.get(order_id)

    if order is None:
        return f"Order {order_id} was not found."

    if not order["refundable"]:
        return f"Order {order_id} is not eligible for a refund."

    return (
        f"Order ID: {order_id}; "
        f"refund amount: {order['amount']:.2f} AED."
    )


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)
agent = create_agent(
    model=model,
    tools=[
        get_order_status,
        calculate_refund,
    ],
    system_prompt=(
        "You are an order-support assistant. "
        "Use the available tools whenever order information is needed. "
        "Do not invent order details. "
        "Answer the customer clearly and concisely."
    ),
)


user_question = (
    "Check the status of order 1002 and tell me "
    "how much money could be refunded."
)


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": user_question,
            }
        ]
    }
)


final_message = result["messages"][-1]

print(final_message.text)