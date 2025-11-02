"""
1. Strategy Pattern Problems
Problem 1: Payment Method Selector

Scenario:
You are building an e-commerce checkout system. Customers can pay via Credit Card, PayPal, or Bank Transfer. Each method has different validation and processing steps.

Goal:
Design a system where adding a new payment method doesn’t require modifying existing code.

Hint:
Encapsulate payment behavior in separate strategy classes implementing a common PaymentStrategy interface.

Problem 2: Character Attack Behaviors (Game)

Scenario:
In a role-playing game, characters can have different attack types (e.g., Sword Attack, Bow Attack, Magic Attack).
Different characters may change their attack type during the game.

Goal:
Implement characters that can switch their attack behavior dynamically.

Hint:
Use a Character class with an AttackBehavior interface and concrete behaviors like SwordAttack, BowAttack, etc.

Problem 3: Sorting Algorithm Chooser

Scenario:
You need to sort data differently depending on the situation (e.g., QuickSort for large datasets, BubbleSort for small ones).
You want to change sorting strategies at runtime based on conditions.

Hint:
Create a SortStrategy interface with implementations like QuickSort, MergeSort, and BubbleSort.

2. Observer Pattern Problems
Problem 4: Stock Market Notifier

Scenario:
You are creating a stock monitoring app. Whenever a stock’s price changes, all subscribed users (observers) must be notified.

Goal:
Implement a publisher-subscriber system where new types of observers (mobile app, web dashboard, etc.) can easily be added.

Hint:
Make Stock the Subject, and investors or dashboards the Observers.

Problem 5: Weather Station

Scenario:
A weather station collects data such as temperature, humidity, and pressure.
You need to display this data on multiple display boards (current conditions, forecast, statistics).

Goal:
Ensure that when weather data updates, all displays automatically update themselves.

Hint:
Make the WeatherData class the Subject, and display elements the Observers.

Problem 6: Chat Room Notifications

Scenario:
In a chat application, when a user sends a message to a group, all other users in that group should receive it instantly.

Goal:
Implement a system where users can join or leave groups dynamically, and only subscribed users get notified of messages.

Hint:
Use ChatRoom as the Subject and each User as an Observer.

3. Decorator Pattern Problems
Problem 7: Coffee Shop (Starbuzz Revisited)

Scenario:
You are designing a beverage ordering system where customers can add condiments (milk, soy, mocha, whip) to their drinks.
Each condiment adds extra cost.

Goal:
Allow adding any combination of condiments without creating a new subclass for each combination.

Hint:
Use a base Beverage component and wrap it dynamically with decorators like Mocha, Whip, etc.

Problem 8: Text Editor with Formatting

Scenario:
You are creating a text editor that allows applying styles like bold, italic, or underline to text.
Users can combine multiple styles.

Goal:
Allow adding or removing styles dynamically without altering the base text class.

Hint:
Use a Text component and decorators like BoldDecorator, ItalicDecorator, etc., that modify the display or rendering.

Problem 9: File Compression and Encryption

Scenario:
You are designing a system that processes data before saving to disk.
Data might need to be compressed, encrypted, or both — depending on user preference.

Goal:
Let users apply any combination of operations to data dynamically.

Hint:
Start with a DataSource interface and decorators like CompressionDecorator and EncryptionDecorator that wrap it.

Problem 10: Web Request Filters

Scenario:
In a web framework, you want to apply filters (like authentication, logging, or compression) to HTTP requests.
Each filter can be applied in different combinations.

Goal:
Allow chaining filters without modifying the core request handler.

Hint:
Wrap the base request handler with decorators implementing the same interface.


"""