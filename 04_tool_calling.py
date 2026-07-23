from dotenv import load_dotenv
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


@tool
def cancel_order(order_id: str) -> str:
    """Cancel an order if it has not already been delivered."""

    order = orders.get(order_id)

    if order is None:
        return f"Order {order_id} was not found."

    if order["status"] == "delivered":
        return f"Order {order_id} cannot be cancelled because it was delivered."

    order["status"] = "cancelled"

    return f"Order {order_id} was cancelled successfully."


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)

tools = [
    get_order_status,
    calculate_refund,
    cancel_order,
]

# Connect every tool name to its actual Python tool
tools_by_name = {
    current_tool.name: current_tool
    for current_tool in tools
}

model_with_tools = model.bind_tools(tools)

user_question = (
    "Check the status of order 1002 and tell me "
    "how much money could be refunded."
)

messages = [
    {
        "role": "user",
        "content": user_question,
    }
]


response = model_with_tools.invoke(messages)
messages.append(response)

for tool_call in response.tool_calls:
    selected_tool = tools_by_name[tool_call["name"]]
    tool_result = selected_tool.invoke(tool_call)
    messages.append(tool_result)

final_response = model_with_tools.invoke(messages)

print(final_response.text)