from tools.flight_tool import search_flights
from backend import run_travel_agent

# rs = search_flights("Plan a 2 days Dubai trip from India")
# print(rs)


user_input = input('Enter travel request')

response = run_travel_agent(user_input=user_input,thread_id='test_user')


print("\n FINAL RESPONSE : \n")
print(response["answer"])