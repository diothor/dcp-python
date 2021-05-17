from datetime import datetime, timedelta


class HitCounter:

    def __init__(self, minutes):
        self.seconds = 60 * minutes
        self.count = 0
        self.hits = [0] * self.seconds
        self.times = [datetime.now() - timedelta(minutes=minutes)] * self.seconds

    # O(1)
    def record(self, timestamp: datetime):
        index = hash(timestamp) % self.seconds
        if self.times[index] != timestamp:
            self.count -= self.hits[index]
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1
        self.count += 1

    # O(1)
    def total(self) -> int:
        return self.count

    # O(n)
    def range(self, lower: datetime, upper: datetime) -> int:
        hit_count = 0
        for i in range(self.seconds):
            if lower <= self.times[i] <= upper:
                hit_count += self.hits[i]
        else:
            return hit_count


test_counter = HitCounter(5)
assert test_counter.total() == 0
test_counter.record(datetime.strptime('05/05/2021', '%m/%d/%Y'))
assert test_counter.total() == 1
test_counter.record(datetime.strptime('05/10/2021', '%m/%d/%Y'))
assert test_counter.total() == 2
test_counter.record(datetime.strptime('05/15/2021', '%m/%d/%Y'))
assert test_counter.total() == 3

assert test_counter.range(datetime.strptime('05/06/2021', '%m/%d/%Y'), datetime.strptime('05/14/2021', '%m/%d/%Y')) == 1
assert test_counter.range(datetime.strptime('05/05/2021', '%m/%d/%Y'), datetime.strptime('05/14/2021', '%m/%d/%Y')) == 2
assert test_counter.range(datetime.strptime('05/05/2021', '%m/%d/%Y'), datetime.strptime('05/15/2021', '%m/%d/%Y')) == 3
assert test_counter.range(datetime.strptime('05/04/2021', '%m/%d/%Y'), datetime.strptime('05/20/2021', '%m/%d/%Y')) == 3
assert test_counter.range(datetime.strptime('05/04/2020', '%m/%d/%Y'), datetime.strptime('05/20/2020', '%m/%d/%Y')) == 0
assert test_counter.range(datetime.strptime('05/04/2022', '%m/%d/%Y'), datetime.strptime('05/20/2022', '%m/%d/%Y')) == 0

test_counter.record(datetime.strptime('05/30/2021', '%m/%d/%Y'))
test_counter.record(datetime.strptime('05/30/2021', '%m/%d/%Y'))
assert test_counter.range(datetime.strptime('05/30/2021', '%m/%d/%Y'), datetime.strptime('05/30/2021', '%m/%d/%Y')) == 2
