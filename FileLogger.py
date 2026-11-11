from abc import ABC, abstractmethod

# 1. التجريد
class ILogger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# 3. التنفيذات المختلفة
class FileLogger(ILogger):
    def log(self, message):
        print(f"Logging to file: {message}")

class DatabaseLogger(ILogger):
    def log(self, message):
        print(f"Logging to database: {message}")

# 2. Application يعتمد على التجريد فقط
class Application:
    def __init__(self, logger: ILogger):
        self.logger = logger

    def start(self):
        self.logger.log("Application started")

# 4. الاستخدام
if __name__ == '__main__':
    app1 = Application(FileLogger())
    app1.start()

    app2 = Application(DatabaseLogger())
    app2.start()