# from multiprocessing import Process,Pool
# import time
# import os
#
# def loop_func(i):
#     print('Run task {}, Child process number({})...'.format(i, os.getpid()))
#     a = 1
#     for i in range(2, 100000):
#         a *= i
#     return a
#
# if __name__ == "__main__":
#     print("Parent process: {}.".format(os.getpid()))
#     start = time.time()
#     p1 = Process(target=loop_func, args=(1,))
#     p2 = Process(target=loop_func, args=(1,))
#     print("Child process will start.")
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time.time()
#     print("Child process end.")
#     print("Task runs {} seconds.".format(end - start))
#
# 普通情况运行程序
# if __name__ == "__main__":
#     print("Parent process: {}.".format(os.getpid()))
#     start = time.time()
#     for i in range(1, 3):
#         p = loop_func(i)
#     end = time.time()
#     print("Child process end.")
#     print("Task runs {} seconds.".format(end - start))
#
# if __name__ == "__main__":
#     print("Parent process: {}.".format(os.getpid()))
#     start = time.time()
#     p = Pool(4)
#     for i in range(1, 6):
#         p.apply_async(loop_func1, args=(i,))
#     print("Child process will start.")
#     p.close()
#     p.join()
#     end = time.time()
#     print("Child process end.")
#     print("Total time {} seconds.".format(end-start))



graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}
print(graph)

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
print(costs)

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
print(parents)
