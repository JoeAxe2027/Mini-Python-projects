def main():
    service_cost = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    services = ["Air freshener", "Rain repellent", "Tire shine", "Wax", "Vacuum"]

    selected_services = []
    while True:
        try:
            print("Avalible service:")
            for i in range(len(services)):
                print(f"{i+1}. {services[i]}")
            service_choice = input("Enter what service you would like, enter 0 if you would like to finsh: ")

            if service_choice == "0":
                break
            elif service_choice.isdigit() and 0 < int(service_choice) <= len(services):
                selected_services.append(services[int(service_choice)-1])
            else:
                print("Please enter a valid service.")
        except (ValueError, IndexError):
            print("Please enter a valid service.")

    base = 10
    total = base
    print(f"Base wash - ${base}")

    for service in selected_services:
        cost = service_cost[service]
        print(f"{service}-${cost}")
        total += cost

    print("----------")
    print(f"Total price - ${total}")

if __name__ == "__main__":
    main()