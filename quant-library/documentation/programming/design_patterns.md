# Design Patterns

- [Design Patterns](#design-patterns)
  - [SOLID Design Principles](#solid-design-principles)
    - [Single Responsibility Principle (SRP)](#single-responsibility-principle-srp)
      - [Simple Example: SRP](#simple-example-srp)
      - [Advanced Example: SRP](#advanced-example-srp)
    - [Open/Closed Principle (OCP)](#openclosed-principle-ocp)
      - [Simple Example: OCP](#simple-example-ocp)
      - [Advanced Example: OCP](#advanced-example-ocp)
    - [Liskov Substitution Principle (LSP)](#liskov-substitution-principle-lsp)
      - [Simple Example: LSP](#simple-example-lsp)
      - [Advanced Example: LSP](#advanced-example-lsp)
    - [Interface Segregation Principle (ISP)](#interface-segregation-principle-isp)
      - [Simple Example: ISP](#simple-example-isp)
      - [Advanced Example: ISP](#advanced-example-isp)
    - [Dependency Inversion Principle (DIP)](#dependency-inversion-principle-dip)
      - [Simple Example: DIP](#simple-example-dip)
      - [Advanced Example: DIP](#advanced-example-dip)
    - [SOLID Principles in Practice](#solid-principles-in-practice)
  - [Gamma Categorization](#gamma-categorization)
    - [Creational](#creational)
    - [Structural](#structural)
    - [Behavioural](#behavioural)
  - [Builder Pattern](#builder-pattern)
    - [Builder Benefits](#builder-benefits)
    - [Builder Use Cases](#builder-use-cases)
    - [Builder Components](#builder-components)
    - [Builder Pattern Example](#builder-pattern-example)
  - [Factory Pattern](#factory-pattern)
    - [Factory Benefits](#factory-benefits)
    - [Factory Use Cases](#factory-use-cases)
    - [Factory Components](#factory-components)
    - [Factory Pattern Example](#factory-pattern-example)
  - [Prototype Pattern](#prototype-pattern)
    - [Prototype Benefits](#prototype-benefits)
    - [Deep Copy vs. Shallow Copy](#deep-copy-vs-shallow-copy)
    - [Prototype Use Cases](#prototype-use-cases)
    - [Prototype Pattern Components](#prototype-pattern-components)
    - [Prototype Pattern Example](#prototype-pattern-example)
    - [Copying through Serialization](#copying-through-serialization)

## SOLID Design Principles

SOLID is an acronym that stands for five key design principles aimed at making software designs more understandable, flexible, and maintainable. These principles were introduced by Robert C. Martin [[2]](../../README.md) and are widely applied in object-oriented programming.

### Single Responsibility Principle (SRP)

> A class should have only one reason to change.

**Explanation**: A class should focus on a single task or responsibility. When a class handles multiple responsibilities, changes in one part of the class may affect other unrelated parts, leading to a higher likelihood of bugs. Classes require fewer test cases and have fewer dependencies.

#### Simple Example: SRP

```csharp
// Violates SRP
public class UserService
{
    public void RegisterUser(User user) { /*...*/ }
    public void SendWelcomeEmail(User user) { /*...*/ }
    public void LogUserActivity(User user) { /*...*/ }
}

// Follows SRP
public class UserService
{
    public void RegisterUser(User user) { /*...*/ }
}

public class EmailService
{
    public void SendWelcomeEmail(User user) { /*...*/ }
}

public class ActivityLogger
{
    public void LogUserActivity(User user) { /*...*/ }
}
```

#### Advanced Example: SRP

```csharp
  // just stores a couple of journal entries and ways of
  // working with them
public class Journal
{
  private readonly List<string> _entries = new List<string>();

  private static int _count = 0;

  public int AddEntry(string text)
  {
    _entries.Add($"{++_count}: {text}");
    return _count; // memento pattern!
  }

  public void RemoveEntry(int index)
  {
    _entries.RemoveAt(index);
  }

  public override string ToString()
  {
    return string.Join(Environment.NewLine, _entries);
  }

  // Save and Load methods break single responsibility principle
  public void Save(string filename, bool overwrite = false)
  {
    File.WriteAllText(filename, ToString());
  }

  public void Load(string filename)
  {
    
  }

  public void Load(Uri uri)
  {
    
  }
}

// handles the responsibility of persisting objects
public class Persistence
{
  public void SaveToFile(Journal journal, string filename, bool overwrite = false)
  {
    if (overwrite || !File.Exists(filename))
      File.WriteAllText(filename, journal.ToString());
  }
}

public class Demo
{
  static void Main(string[] args)
  {
    var j = new Journal();
    j.AddEntry("I cried today.");
    j.AddEntry("I ate a bug.");
    WriteLine(j);

    var p = new Persistence();
    var filename = @"c:\temp\journal.txt";
    p.SaveToFile(j, filename);
    Process.Start(filename);
  }
}
```

### Open/Closed Principle (OCP)

> Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

**Explanation**: You should be able to add new functionality to a class or module without modifying its existing code. This can be achieved using inheritance, interfaces, or other design patterns that promote extension.

#### Simple Example: OCP

```csharp
// Violates OCP
public class PaymentProcessor
{
    public void ProcessPayment(string paymentType)
    {
        if (paymentType == "CreditCard")
        {
            // Process credit card payment
        }
        else if (paymentType == "PayPal")
        {
            // Process PayPal payment
        }
    }
}

// Follows OCP
public interface IPaymentMethod
{
    void ProcessPayment();
}

public class CreditCardPayment : IPaymentMethod
{
    public void ProcessPayment() { /*...*/ }
}

public class PayPalPayment : IPaymentMethod
{
    public void ProcessPayment() { /*...*/ }
}

public class PaymentProcessor
{
    public void ProcessPayment(IPaymentMethod paymentMethod)
    {
        paymentMethod.ProcessPayment();
    }
}
```

#### Advanced Example: OCP

```csharp
public enum Color
{
  Red, Green, Blue
}

public enum Size
{
  Small, Medium, Large, Huge
}

public class Product
{
  public string Name;
  public Color Color;
  public Size Size;

  public Product(string name, Color color, Size size)
  {
    Name = name ?? throw new ArgumentNullException(paramName: nameof(name));
    Color = color;
    Size = size;
  }
}

public class ProductFilter
{
  // let's suppose we don't want ad-hoc queries on products
  public static IEnumerable<Product> FilterByColor(IEnumerable<Product> products, Color color)
  {
    foreach (var p in products)
      if (p.Color == color)
        yield return p;
  }
  
  public static IEnumerable<Product> FilterBySize(IEnumerable<Product> products, Size size)
  {
    foreach (var p in products)
      if (p.Size == size)
        yield return p;
  }

  public static IEnumerable<Product> FilterBySizeAndColor(IEnumerable<Product> products, Size size, Color color)
  {
    foreach (var p in products)
      if (p.Size == size && p.Color == color)
        yield return p;
  } // state space explosion - the number of possible configurations or states in a system increases exponentially as the number of variables/parameters grows. 
    // 3 criteria = 7 methods

  // OCP = open for extension but closed for modification
}

// we introduce two new interfaces that are open for extension

public interface ISpecification<T>
{
  bool IsSatisfied(Product p);
}

public interface IFilter<T>
{
  IEnumerable<T> Filter(IEnumerable<T> items, ISpecification<T> spec);
}

public class ColorSpecification : ISpecification<Product>
{
  private Color _color;

  public ColorSpecification(Color color)
  {
    _color = color;
  }

  public bool IsSatisfied(Product p)
  {
    return p.Color == _color;
  }
}

public class SizeSpecification : ISpecification<Product>
{
  private Size _size;

  public SizeSpecification(Size size)
  {
    _size = size;
  }

  public bool IsSatisfied(Product p)
  {
    return p.Size == _size;
  }
}

// combinator
public class AndSpecification<T> : ISpecification<T>
{
  private ISpecification<T> _first, _second;

  public AndSpecification(ISpecification<T> first, ISpecification<T> second)
  {
    _first = first ?? throw new ArgumentNullException(paramName: nameof(first));
    _second = second ?? throw new ArgumentNullException(paramName: nameof(second));
  }

  public bool IsSatisfied(Product p)
  {
    return _first.IsSatisfied(p) && _second.IsSatisfied(p);
  }
}

public class BetterFilter : IFilter<Product>
{
  public IEnumerable<Product> Filter(IEnumerable<Product> items, ISpecification<Product> spec)
  {
    foreach (var i in items)
      if (spec.IsSatisfied(i))
        yield return i;
  }
}

public class Demo
{
  static void Main(string[] args)
  {
    var apple = new Product("Apple", Color.Green, Size.Small);
    var tree = new Product("Tree", Color.Green, Size.Large);
    var house = new Product("House", Color.Blue, Size.Large);

    Product[] products = {apple, tree, house};

    // BEFORE
    var pf = new ProductFilter();
    WriteLine("Green products (old):");
    foreach (var p in pf.FilterByColor(products, Color.Green))
      WriteLine($" - {p.Name} is green");


    // vv AFTER
    var bf = new BetterFilter();
    WriteLine("Green products (new):");
    foreach (var p in bf.Filter(products, new ColorSpecification(Color.Green)))
      WriteLine($" - {p.Name} is green");

    WriteLine("Large products");
    foreach (var p in bf.Filter(products, new SizeSpecification(Size.Large)))
      WriteLine($" - {p.Name} is large");

    WriteLine("Large blue items");
    foreach (var p in bf.Filter(products,
      new AndSpecification<Product>(new ColorSpecification(Color.Blue), new SizeSpecification(Size.Large)))
    )
    {
      WriteLine($" - {p.Name} is big and blue");
    }
  }
}
```

### Liskov Substitution Principle (LSP)

> Subtypes must be substitutable for their base types.

**Explanation**: Derived classes should extend the base class without changing its behaviour in a way that affects the client using the base class.

#### Simple Example: LSP

```csharp
// Violates LSP
public class Bird
{
    public virtual void Fly() { /*...*/ }
}

public class Penguin : Bird
{
    public override void Fly()
    {
        throw new NotImplementedException();
    }
}

// Follows LSP
public abstract class Bird
{
    public abstract void Move();
}

public class Sparrow : Bird
{
    public override void Move() { /*...*/ } // Fly
}

public class Penguin : Bird
{
    public override void Move() { /*...*/ } // Swim
}
```

#### Advanced Example: LSP

```csharp
// using a classic example
public class Rectangle
{
  //public int Width { get; set; }
  //public int Height { get; set; }

  public virtual int Width { get; set; }
  public virtual int Height { get; set; }

  public Rectangle()
  {
    
  }

  public Rectangle(int width, int height)
  {
    Width = width;
    Height = height;
  }

  public override string ToString()
  {
    return $"{nameof(Width)}: {Width}, {nameof(Height)}: {Height}";
  }
}

public class Square : Rectangle
{
  //public new int Width
  //{
  //  set { base.Width = base.Height = value; }
  //}

  //public new int Height
  //{ 
  //  set { base.Width = base.Height = value; }
  //}

  public override int Width // nasty side effects
  {
    set { base.Width = base.Height = value; }
  }

  public override int Height
  { 
    set { base.Width = base.Height = value; }
  }
}

public class Demo
{
  static public int Area(Rectangle r) => r.Width * r.Height;

  static void Main(string[] args)
  {
    Rectangle rc = new Rectangle(2,3);
    WriteLine($"{rc} has area {Area(rc)}");

    // should be able to substitute a base type for a subtype
    /*Square*/ Rectangle sq = new Square();
    sq.Width = 4;
    WriteLine($"{sq} has area {Area(sq)}");
  }
}
```

### Interface Segregation Principle (ISP)

> Clients should not be forced to depend on interfaces they do not use.

**Explanation**: Large, general-purpose interfaces should be split into smaller, more specific ones so that clients only need to implement what they actually use.

#### Simple Example: ISP

```csharp
// Violates ISP
public interface IWorker
{
    void Work();
    void Eat();
}

public class Robot : IWorker
{
    public void Work() { /*...*/ }
    public void Eat()
    {
        throw new NotImplementedException();
    }
}

// Follows ISP
public interface IWorkable
{
    void Work();
}

public interface IFeedable
{
    void Eat();
}

public class Human : IWorkable, IFeedable
{
    public void Work() { /*...*/ }
    public void Eat() { /*...*/ }
}

public class Robot : IWorkable
{
    public void Work() { /*...*/ }
}
```

#### Advanced Example: ISP

```csharp
public class Document
{
}

public interface IMachine
{
  void Print(Document d);
  void Fax(Document d);
  void Scan(Document d);
}

// ok if you need a multifunction machine
public class MultiFunctionPrinter : IMachine
{
  public void Print(Document d)
  {
    //
  }

  public void Fax(Document d)
  {
    //
  }

  public void Scan(Document d)
  {
    //
  }
}

public class OldFashionedPrinter : IMachine
{
  public void Print(Document d)
  {
    // yep
  }

  public void Fax(Document d)
  {
    throw new System.NotImplementedException();
  }

  public void Scan(Document d)
  {
    throw new System.NotImplementedException();
  }
}

public interface IPrinter
{
  void Print(Document d);
}

public interface IScanner
{
  void Scan(Document d);
}

public class Printer : IPrinter
{
  public void Print(Document d)
  {
    
  }
}

public class Photocopier : IPrinter, IScanner
{
  public void Print(Document d)
  {
    throw new System.NotImplementedException();
  }

  public void Scan(Document d)
  {
    throw new System.NotImplementedException();
  }
}

public interface IMultiFunctionDevice : IPrinter, IScanner //
{
  
}

public struct MultiFunctionMachine : IMultiFunctionDevice
{
  // compose this out of several modules
  private IPrinter _printer;
  private IScanner _scanner;

  public MultiFunctionMachine(IPrinter printer, IScanner scanner)
  {
    if (printer == null)
    {
      throw new ArgumentNullException(paramName: nameof(printer));
    }
    if (scanner == null)
    {
      throw new ArgumentNullException(paramName: nameof(scanner));
    }
    _printer = printer;
    _scanner = scanner;
  }

  public void Print(Document d)
  {
    _printer.Print(d);
  }

  public void Scan(Document d)
  {
    _scanner.Scan(d);
  }
}
```

### Dependency Inversion Principle (DIP)

> A. High-level modules should not depend on low-level modules. Both should depend on abstractions.
>
> B. Abstractions should not depend upon details. Details should depend upon abstractions.

**Explanation**: This principle suggests that classes should depend on interfaces or abstract classes rather than concrete classes, promoting loose coupling.

#### Simple Example: DIP

```csharp
// Violates DIP
public class FileLogger
{
    public void Log(string message) { /*...*/ }
}

public class UserService
{
    private FileLogger _logger = new FileLogger();

    public void RegisterUser(User user)
    {
        _logger.Log("User registered.");
        // Registration logic...
    }
}

// Follows DIP
public interface ILogger
{
    void Log(string message);
}

public class FileLogger : ILogger
{
    public void Log(string message) { /*...*/ }
}

public class DatabaseLogger : ILogger
{
    public void Log(string message) { /*...*/ }
}

public class UserService
{
    private readonly ILogger _logger;

    public UserService(ILogger logger)
    {
        _logger = logger;
    }

    public void RegisterUser(User user)
    {
        _logger.Log("User registered.");
        // Registration logic...
    }
}
```

#### Advanced Example: DIP

```csharp
// high-level modules should not depend on low-level; both should depend on abstractions
// abstractions should not depend on details; details should depend on abstractions

public enum Relationship
{
  Parent,
  Child,
  Sibling
}

public class Person
{
  public string Name;
  // public DateTime DateOfBirth;
}

public interface IRelationshipBrowser
{
  IEnumerable<Person> FindAllChildrenOf(string name);
}

public class Relationships : IRelationshipBrowser // low-level
{
  private List<(Person,Relationship,Person)> _relations
    = new List<(Person, Relationship, Person)>();

  public void AddParentAndChild(Person parent, Person child)
  {
    _relations.Add((parent, Relationship.Parent, child));
    _relations.Add((child, Relationship.Child, parent));
  }

  public List<(Person, Relationship, Person)> Relations => _relations;

  public IEnumerable<Person> FindAllChildrenOf(string name)
  {
    return _relations
      .Where(x => x.Item1.Name == name
                  && x.Item2 == Relationship.Parent).Select(r => r.Item3);
  }
}

public class Research
{
  public Research(Relationships relationships) 
  {
    // high-level: find all of john's children
    //var relations = relationships.Relations;
    //foreach (var r in relations
    //  .Where(x => x.Item1.Name == "John"
    //              && x.Item2 == Relationship.Parent))
    //{
    //  WriteLine($"John has a child called {r.Item3.Name}");
    //}
  }

  public Research(IRelationshipBrowser browser) {
    foreach (var p in browser.FindAllChildrenOf("John"))
    {
      WriteLine($"John has a child called {p.Name}");
    }
  }

  static void Main(string[] args)
  {
    var parent = new Person {Name = "John"};
    var child1 = new Person {Name = "Chris"};
    var child2 = new Person {Name = "Matt"};

    // low-level module
    var relationships = new Relationships();
    relationships.AddParentAndChild(parent, child1);
    relationships.AddParentAndChild(parent, child2);

    new Research(relationships);
    
  }
}
```

### SOLID Principles in Practice

```csharp
// Step 1: Define the core entities and interfaces

// SRP: Each class has a single responsibility
public class Order
{
    public int Id { get; set; }
    public List<OrderItem> Items { get; set; }
    public decimal TotalAmount { get; set; }

    public void CalculateTotal()
    {
        TotalAmount = Items.Sum(item => item.Price * item.Quantity);
    }
}

public class OrderItem
{
    public string Name { get; set; }
    public decimal Price { get; set; }
    public int Quantity { get; set; }
}

// OCP: Payment methods can be extended without modifying existing code
public interface IPaymentMethod
{
    void Pay(decimal amount);
}

public class CreditCardPayment : IPaymentMethod
{
    public void Pay(decimal amount)
    {
        // Process credit card payment
        Console.WriteLine($"Paid {amount} using Credit Card.");
    }
}

public class PayPalPayment : IPaymentMethod
{
    public void Pay(decimal amount)
    {
        // Process PayPal payment
        Console.WriteLine($"Paid {amount} using PayPal.");
    }
}

// LSP: Derived classes can replace base classes without altering behaviour
public abstract class Discount
{
    public abstract decimal Apply(decimal amount);
}

public class NoDiscount : Discount
{
    public override decimal Apply(decimal amount)
    {
        return amount;
    }
}

public class PercentageDiscount : Discount
{
    private readonly decimal _percentage;

    public PercentageDiscount(decimal percentage)
    {
        _percentage = percentage;
    }

    public override decimal Apply(decimal amount)
    {
        return amount - (amount * _percentage / 100);
    }
}

// ISP: Interfaces are split into smaller ones so that classes implement only what they need
public interface IOrderService
{
    void ProcessOrder(Order order, IPaymentMethod paymentMethod);
}

public interface IOrderNotificationService
{
    void NotifyOrderProcessed(Order order);
}

public interface IOrderDiscountService
{
    decimal ApplyDiscount(Order order, Discount discount);
}

// DIP: High-level modules depend on abstractions, not concrete implementations
public class OrderService : IOrderService
{
    private readonly IOrderNotificationService _notificationService;
    private readonly IOrderDiscountService _discountService;

    public OrderService(IOrderNotificationService notificationService, IOrderDiscountService discountService)
    {
        _notificationService = notificationService;
        _discountService = discountService;
    }

    public void ProcessOrder(Order order, IPaymentMethod paymentMethod)
    {
        order.CalculateTotal();

        // Apply a discount
        decimal totalAmount = _discountService.ApplyDiscount(order, new PercentageDiscount(10));

        // Process payment
        paymentMethod.Pay(totalAmount);

        // Notify the customer
        _notificationService.NotifyOrderProcessed(order);
    }
}

// Notification service (demonstrating DIP)
public class EmailNotificationService : IOrderNotificationService
{
    public void NotifyOrderProcessed(Order order)
    {
        // Send notification
        Console.WriteLine($"Order {order.Id} processed. Notification sent via Email.");
    }
}

// Discount service (demonstrating DIP)
public class OrderDiscountService : IOrderDiscountService
{
    public decimal ApplyDiscount(Order order, Discount discount)
    {
        return discount.Apply(order.TotalAmount);
    }
}

// Usage example
class Program
{
    static void Main(string[] args)
    {
        var order = new Order
        {
            Id = 1,
            Items = new List<OrderItem>
            {
                new OrderItem { Name = "Laptop", Price = 1000, Quantity = 1 },
                new OrderItem { Name = "Mouse", Price = 50, Quantity = 2 }
            }
        };

        var notificationService = new EmailNotificationService();
        var discountService = new OrderDiscountService();

        var orderService = new OrderService(notificationService, discountService);

        // Process the order using a Credit Card
        orderService.ProcessOrder(order, new CreditCardPayment());

        // Process the order using PayPal
        orderService.ProcessOrder(order, new PayPalPayment());
    }
}
```

1. Single Responsibility Principle (SRP):

   - `Order` and `OrderItem` classes handle only order-related data.
   - `OrderService` class handles order processing.
   - `EmailNotificationService` handles sending notifications.
   - `OrderDiscountService` handles applying discounts.

2. Open/Closed Principle (OCP):

    - The `IPaymentMethod` interface allows for new payment methods (e.g., `CreditCardPayment`, `PayPalPayment`) without modifying the existing code.
    - The `Discount` class can be extended with new discount types (e.g., `PercentageDiscount`, `NoDiscount`) without changing existing functionality.

3. Liskov Substitution Principle (LSP):

   - The Discount subclasses (NoDiscount, PercentageDiscount) can be used interchangeably without altering the correctness of the program.

4. Interface Segregation Principle (ISP):

   - Interfaces `IOrderService`, `IOrderNotificationService`, and `IOrderDiscountService` are specific, ensuring that classes implementing them only need to focus on relevant responsibilities.

5. Dependency Inversion Principle (DIP):

    - The `OrderService` class depends on the abstractions (`IOrderNotificationService`, `IOrderDiscountService`, `IPaymentMethod`) rather than concrete implementations, promoting flexibility and testability.

## Gamma Categorization

Design patterns are typically split into one of the following three categories: *creational*, *structural*, and *behavioural*.

### Creational

- Focus on the creation (construction) of objects.
- Explicit (constructor) versus implicit (dependency injection, reflection, etc.)
- Wholesale (single statement) versus piecewise (step-by-step)

### Structural

- Concerned with the structure of code - e.g. class members.
- Wrappers which mimic the underlying class's interface.
- Stress the importance of good API design.

### Behavioural

- No central theme to these patterns, each will solve specific problems.

## Builder Pattern

The Builder Pattern is a design pattern that provides a way to construct complex objects step-by-step. It allows for the construction process to be separated from the actual representation of the object, making it easier to create different representations of an object using the same construction process.

### Builder Benefits

- **Separation of Concerns:**
  - The Builder Pattern separates the construction logic from the representation of a complex object.
  - Makes the code easier to manage and understand by isolating construction from representation.

- **Flexibility in Object Construction:**
  - Allows for creating different representations of an object using the same construction process.
  - Enables different configurations of an object without modifying the construction code.

- **Immutability:**
  - Facilitates the creation of immutable objects (if designed this way).
  - Ensures that once an object is built, it cannot be altered, reducing bugs related to unintended modifications.

- **Enhanced Readability:**
  - Improves code readability by providing a clear, step-by-step construction process.
  - Makes it apparent which components are being added and in what order.

- **Encapsulation of Construction Logic:**
  - Encapsulates complex construction logic within the builder.
  - Simplifies client code by hiding intricate details of object creation.

- **Ease of Maintenance:**
  - Changes to the construction process or representation are managed in one place (within the builder or director).
  - Simplifies maintenance and modification by centralizing construction logic.

### Builder Use Cases

- **Complex Object Creation:**
  - Suitable for constructing objects with many optional components or configurations.
  - Example: Creating a configuration object with multiple settings.

- **Different Representations of an Object:**
  - Useful for building different versions of an object with varying details.
  - Example: Generating summary and detailed reports using a common construction process.

- **Immutable Objects:**
  - Ideal for designing objects that should not change after creation.
  - Example: Creating a settings object where all necessary fields are set during the build process.

- **Constructing Complex Strings:**
  - Effective for building complex strings or documents with multiple sections.
  - Example: Creating a formatted email or report with various parts (e.g., subject, body, signature).

- **Fluent Interface Design:**
  - Supports a fluent interface, allowing method chaining for object construction.
  - Example: Using a builder with method chaining to construct an object in a clean and readable manner.

- **Encapsulation of Construction Logic:**
  - Encapsulates intricate construction logic within a builder, keeping it separate from the rest of the code.
  - Example: Managing complex object creation within a dedicated builder class.

- **Testing and Mocking:**
  - Simplifies unit testing and mocking by allowing specific configurations of objects.
  - Example: Creating objects with particular settings for test scenarios.

### Builder Components

1. **Builder**: An interface or abstract class that defines the steps required to build a product.
2. **ConcreteBuilder**: A class that implements the `Builder` interface and constructs the product.
3. **Product**: The complex object that is being constructed.
4. **Director**: A class that constructs an object using the `Builder` interface. It directs the building process.

### Builder Pattern Example

Let's say we want to construct a report with different sections such as a title, introduction, body, and conclusion. Using the Builder Pattern, we can build this report step-by-step with various configurations.

```csharp
using System.Text;

// Product
public class Report
{
    private StringBuilder _stringBuilder = new StringBuilder();

    public void AddTitle(string title) => _stringBuilder.AppendLine($"Title: {title}");
    public void AddIntroduction(string introduction) => _stringBuilder.AppendLine($"Introduction: {introduction}");
    public void AddBody(string body) => _stringBuilder.AppendLine($"Body: {body}");
    public void AddConclusion(string conclusion) => _stringBuilder.AppendLine($"Conclusion: {conclusion}");

    public override string ToString() => _stringBuilder.ToString();
}

// Builder Interface
public interface IReportBuilder
{
    void SetTitle(string title);
    void SetIntroduction(string introduction);
    void SetBody(string body);
    void SetConclusion(string conclusion);
    Report Build();
}

// Concrete Builder
public class DetailedReportBuilder : IReportBuilder
{
    private Report _report = new Report();

    public void SetTitle(string title) => _report.AddTitle(title);
    public void SetIntroduction(string introduction) => _report.AddIntroduction(introduction);
    public void SetBody(string body) => _report.AddBody(body);
    public void SetConclusion(string conclusion) => _report.AddConclusion(conclusion);

    public Report Build() => _report;
}

// Director
public class ReportDirector
{
    private readonly IReportBuilder _builder;

    public ReportDirector(IReportBuilder builder)
    {
        _builder = builder;
    }

    public void ConstructFullReport()
    {
        _builder.SetTitle("Annual Report");
        _builder.SetIntroduction("This is the introduction to the annual report.");
        _builder.SetBody("This section contains the main body of the report.");
        _builder.SetConclusion("This is the conclusion of the report.");
    }
}

// Client Code
class Program
{
    static void Main(string[] args)
    {
        IReportBuilder builder = new DetailedReportBuilder();
        ReportDirector director = new ReportDirector(builder);

        director.ConstructFullReport();
        Report report = builder.Build();

        Console.WriteLine(report);
    }
}
```

## Factory Pattern

The Factory Pattern is a design pattern used to create objects without specifying the exact class of the object that will be created. It provides a way to delegate the instantiation logic to a factory method or class, allowing for more flexible and maintainable object creation.

### Factory Benefits

- **Encapsulation of Object Creation:**
  - Encapsulates the instantiation logic of objects in a factory method or class.
  - Hides the details of the object's creation from the client code.

- **Flexibility:**
  - Allows for the creation of objects based on varying conditions or configurations.
  - Makes it easier to introduce new types of objects without changing the client code.

- **Decoupling:**
  - Reduces the coupling between the client code and the concrete classes.
  - The client code interacts with an abstract factory or interface rather than specific implementations.

- **Centralized Object Creation:**
  - Centralizes the logic for creating objects, making it easier to manage and update.
  - Facilitates changes to object creation logic in one place without affecting the client code.

- **Promotes Open/Closed Principle:**
  - Supports the Open/Closed Principle by allowing the system to be open for extension (new products) but closed for modification (existing client code).

### Factory Use Cases

- **Complex Object Creation:**
  - Useful when creating objects involves complex initialization or configuration.
  - Example: Creating different types of documents (e.g., PDFs, Word documents) with specific formats.

- **Object Creation Based on Input:**
  - Ideal for creating objects based on user input or other runtime conditions.
  - Example: Creating different shapes (e.g., circles, squares) based on user selection in a drawing application.

- **Polymorphic Object Creation:**
  - Useful when different classes share a common interface or base class, and the specific class to instantiate is determined at runtime.
  - Example: Creating different types of vehicles (e.g., cars, trucks) based on user input.

- **Code Decoupling:**
  - Helps in decoupling the code that uses the objects from the code that creates the objects.
  - Example: Separating the object creation logic from the business logic that uses the objects.

- **Testing and Mocking:**
  - Facilitates testing and mocking by providing a way to easily swap out concrete implementations with mock objects or stubs.
  - Example: Using a factory to create mock services for unit testing.

### Factory Components

- **Factory Interface:**
  - Defines a method for creating objects. The method typically returns an abstract type or interface.

- **ConcreteFactory:**
  - Implements the factory interface and provides the logic for creating concrete objects.

- **Product Interface:**
  - Defines the interface or abstract class that the products must adhere to.

- **ConcreteProduct:**
  - Implements the product interface or extends the abstract class. These are the actual objects created by the factory.

### Factory Pattern Example

Consider a scenario where we need to create different types of notifications, such as email and SMS notifications. We can use the Factory Pattern to create these notifications based on user preferences.

```csharp
// Product Interface
public interface INotification
{
    void Send(string message);
}

// Concrete Products
public class EmailNotification : INotification
{
    public void Send(string message) => Console.WriteLine($"Sending email with message: {message}");
}

public class SmsNotification : INotification
{
    public void Send(string message) => Console.WriteLine($"Sending SMS with message: {message}");
}

// Factory Interface
public interface INotificationFactory
{
    INotification CreateNotification();
}

// Concrete Factories
public class EmailNotificationFactory : INotificationFactory
{
    public INotification CreateNotification() => new EmailNotification();
}

public class SmsNotificationFactory : INotificationFactory
{
    public INotification CreateNotification() => new SmsNotification();
}

// Client Code
class Program
{
    static void Main(string[] args)
    {
        INotificationFactory factory;
        string notificationType = "Email"; // This could be input from user or configuration

        if (notificationType == "Email")
        {
            factory = new EmailNotificationFactory();
        }
        else
        {
            factory = new SmsNotificationFactory();
        }

        INotification notification = factory.CreateNotification();
        notification.Send("Hello, Factory Pattern!");
    }
}
```

## Prototype Pattern

- The Prototype Pattern is a creational design pattern that enables object creation by cloning existing instances.
- Instead of creating new objects from scratch, this pattern allows copying an existing object to create new instances with similar properties.
- This reduces the overhead associated with instantiating objects and provides a way to create objects efficiently.

### Prototype Benefits

- Efficient Object Creation:
  - Reduces the cost of creating objects from scratch by cloning an existing instance.
  - Saves resources when complex objects or large data structures are involved.
- Dynamic Object Creation:
  - Provides flexibility to create new objects dynamically without knowing their exact class.
  - Enables runtime object creation without tightly coupling code to specific implementations.
- Decoupling from Concrete Classes:
  - Decouples the code from concrete classes by interacting with cloned instances.
  - Allows the system to work with abstractions, enhancing flexibility and maintainability.
- Object State Preservation:
  - Ensures that cloned objects maintain the state of the original instance.
  - Facilitates the creation of objects with similar initial states.

### Deep Copy vs. Shallow Copy

- Shallow Copy:
  - Copies the values and references on an object without duplicating the referenced objects.
  - The cloned object shares references with the original, leading to shared mutable data.
  - Changes made to mutable objects in one instance affect the other instance.
- Deep Copy:
  - Copies an object along with all nested objects it references, creating independent copies.
  - Ensures that cloned objects do not share mutable data with the original instance.
  - Changes to nested objects in one instance do not impact the other instance.

### Prototype Use Cases

- Object Creation with Varying States:
  - Useful when there is a need to create objects with slightly different states but similar structures.
  - Example: Creating multiple types of trees with the same basic structure but different leaf colors.
- Expensive Object Creation:
  - Ideal for creating objects that involve costly or resource-intensive instantiation processes.
  - Example: Duplicating large graphical objects in a game to avoid complex recalculations.
- Preserving Original Object State:
  - Useful when the original state of an object needs to be preserved, while creating similar objects for modifications.
  - Example: Cloning a complex document to apply changes while keeping the original version unchanged.

### Prototype Pattern Components

- Prototype Interface:
  - Defines a method for cloning objects, typically named Clone or Copy.
- Concrete Prototype:
  - Implements the prototype interface and defines how the cloning should be performed.
- Client:
  - Uses the prototype to create new instances by cloning an existing object.

### Prototype Pattern Example

```csharp
public interface IDeepCopyable<T> where T : new()
{
  void CopyTo(T target);
  
  public T DeepCopy() // default interface method
  {
    T t = new T();
    CopyTo(t);
    return t;
  }
}

public class Address : IDeepCopyable<Address>
{
  public string StreetName { get; set; }
  public int HouseNumber { get; set; }

  public Address(string streetName, int houseNumber)
  {
    StreetName = streetName;
    HouseNumber = houseNumber;
  }

  public Address()
  {
    
  }

  public void CopyTo(Address target)
  {
    target.StreetName = StreetName;
    target.HouseNumber = HouseNumber;
  }
}



public class Person : IDeepCopyable<Person>
{
  public string[] Names { get; set; }
  public Address Address { get; set; }

  public Person()
  {
    
  }
  
  public Person(string[] names, Address address)
  {
    Names = names;
    Address = address;
  }

  public virtual void CopyTo(Person target)
  {
    target.Names = (string[]) Names.Clone();
    target.Address = Address.DeepCopy();
  }
}

public class Employee : Person, IDeepCopyable<Employee>
{
  public int Salary { get; set; }

  public void CopyTo(Employee target)
  {
    base.CopyTo(target);
    target.Salary = Salary;
  }
}

public static class DeepCopyExtensions
{
  public static T DeepCopy<T>(this IDeepCopyable<T> item) 
    where T : new()
  {
    return item.DeepCopy();
  }

  public static T DeepCopy<T>(this T person)
    where T : Person, new()
  {
    return ((IDeepCopyable<T>) person).DeepCopy();
  }
}

public static class Demo
{
  static void Main()
  {
    var john = new Employee();
    john.Names = new[] {"John", "Doe"};
    john.Address = new Address {HouseNumber = 123, StreetName = "London Road"};
    john.Salary = 321000;
    var copy = john.DeepCopy();

    copy.Names[1] = "Smith";
    copy.Address.HouseNumber++;
    copy.Salary = 123000;
    
    Console.WriteLine(john);
    Console.WriteLine(copy);
  }
}
```

### Copying through Serialization

- Copying through serialization involves creating a deep copy of an object by serializing it into a data format (such as JSON, XML, or binary) and then deserializing it back into a new object.
- This method creates an exact replica of the original object, including all nested objects, ensuring that the new copy is independent of the original.
- Benefits
  - Automatic Deep Copy:
    - Automatically handles nested objects, creating completely independent copies.
    - Ideal when objects have complex nested structures or when creating deep copies manually is cumbersome.
  - No Need for Manual Copy Logic:
    - Relieves developers from writing manual deep copy logic, reducing maintenance and potential errors.
- Drawbacks
  - Performance Overhead:
    - Serialization and deserialization can be slower compared to manual copying techniques, especially for large or complex objects.
    - Involves memory overhead due to the temporary serialized format.
  - Serializable Restrictions:
    - Requires objects to be marked as serializable, and all nested objects must also support serialization.
    - May not work with non-serializable objects or those with transient fields.

```csharp
public static class ExtensionMethods
{
  public static T DeepCopy<T>(this T self)
  {
    MemoryStream stream = new MemoryStream();
    BinaryFormatter formatter = new BinaryFormatter();
    formatter.Serialize(stream, self);
    stream.Seek(0, SeekOrigin.Begin);
    object copy = formatter.Deserialize(stream);
    stream.Close();
    return (T)copy;
  }

  public static T DeepCopyXml<T>(this T self)
  {
    using (var ms = new MemoryStream())
    {
      XmlSerializer s = new XmlSerializer(typeof(T));
      s.Serialize(ms, self);
      ms.Position = 0;
      return (T) s.Deserialize(ms);
    }
  }
}

[Serializable] // this is, unfortunately, required
public class Foo
{
  public uint Stuff { get; set; }
  public string Whatever { get; set; }
}

public static class CopyThroughSerialization
{
  static void Main()
  {
    Foo foo = new Foo {Stuff = 42, Whatever = "abc"};

    //Foo foo2 = foo.DeepCopy(); // crashes without [Serializable]
    Foo foo2 = foo.DeepCopyXml();

    foo2.Whatever = "xyz";
    WriteLine(foo);
    WriteLine(foo2);
  }
}
```