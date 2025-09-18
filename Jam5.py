class RecentCounter:
    def init(self):
        self.request_times = []

    def ping(self, t: int) -> int:
        self.request_times.append(t)
        
        # Удаляем все запросы, которые произошли раньше чем (t - 3000)
        start_time = t - 3000
        while self.request_times and self.request_times[0] < start_time:
            self.request_times.pop(0)
            
        return len(self.request_times)
