def solution(messenger, whoami):
    # MPI
    # send all messages to 1
    if whoami > 1:
        min_val = messenger.get_item(0)
        for i in range(1, messenger.get_data_size(), 1):  # starting from the second elements
            if min_val > messenger.get_item(i):
                min_val = messenger.get_item(i)
        messenger.send_message(1, str(min_val).encode())  # send it to id 1 the smallest value

    else:  # id 1
        min_val = messenger.get_item(0)
        for i in range(1, messenger.get_data_size(), 1):
            if min_val > messenger.get_item(i):
                min_val = messenger.get_item(i)
            if min_val == 1:
                messenger.record_result(min_val)  # the smallest it could be is 1

        for i in range(4):  # repeat this process 4 times (for each id)
            received_min = int(messenger.receive_message().decode())
            if min_val > received_min:
                min_val = received_min
            if min_val == 1:
                messenger.record_result(min_val)  # the smallest it could be is 1

        messenger.record_result(min_val)  # return by program 1

