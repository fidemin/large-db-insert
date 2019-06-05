from math import log

class ChunkSizeGenerator(object):
    def __init__(self, start_chunk_size, num_of_indexes, *, limit=0, alpha=1):
        self._start_chunk_size = start_chunk_size
        self._num_of_indexes = num_of_indexes
        self._limit = limit
        self._alpha = alpha

        self._it = self._iterator()

    def _iterator(self):
        chunk = self._start_chunk_size
        num_of_indexes = self._num_of_indexes
        limit = self._limit
        alpha = self._alpha


        yield max(limit, chunk)
        total = chunk

        while True:
            chunk = int(chunk *(1+(num_of_indexes) + num_of_indexes * log(total)) /\
                        (alpha * (1+num_of_indexes + num_of_indexes * log(total + chunk))))
            total += chunk
            yield max(chunk, limit)

    def chunk(self):
        return next(self._it)


if __name__ == '__main__':
    # example
    gen = ChunkSizeGenerator(100000, 1, limit=1000, alpha=1.001)

    for _ in range(100):
        print(gen.chunk())
