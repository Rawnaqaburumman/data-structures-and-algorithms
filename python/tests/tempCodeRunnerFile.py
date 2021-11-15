
# def test_pseudo_queue_enqueue_value(pseudo_queue_1):
#    stack1=Stack()
#   stack2=Stack()
#   stack1.push(1)
#   stack1.push(2)
#   stack1.push(3)
#     expected = 1
#     # Act
#     actual = pseudo_queue_1.dequeue()
#     # Assert
#     assert actual == expected


# def test_pseudo_queue_enqueue_multiple(pseudo_queue):
#     # Arrange
#     expected_1 = 0
#     expected_2 = 7
#     # Act
#     actual_1 = pseudo_queue.dequeue()
#     actual_2 = pseudo_queue.dequeue()
#     # Assert
#     assert actual_1 == expected_1
#     assert expected_2 == actual_2


# def test_pseudo_dequeue_value(pseudo_queue):
#     # Arrange
#     expected = 0
#     # Act
#     actual = pseudo_queue.dequeue()
#     # Assert
#     assert actual == expected


# def test_pseudo_dequeue_multiple(pseudo_queue):
#     pseudo_queue.dequeue()
#     pseudo_queue.dequeue()
#     pseudo_queue.dequeue()
#     pseudo_queue.dequeue()
#     pseudo_queue.dequeue()
#     with pytest.raises(Exception):
#         assert pseudo_queue.dequeue()