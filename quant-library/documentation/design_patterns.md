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
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using static System.Console;

namespace DotNetDesignPatternDemos.SOLID.SRP
{
  // just stores a couple of journal entries and ways of
  // working with them
  public class Journal
  {
    private readonly List<string> entries = new List<string>();

    private static int count = 0;

    public int AddEntry(string text)
    {
      entries.Add($"{++count}: {text}");
      return count; // memento pattern!
    }

    public void RemoveEntry(int index)
    {
      entries.RemoveAt(index);
    }

    public override string ToString()
    {
      return string.Join(Environment.NewLine, entries);
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
using System;
using System.Collections.Generic;
using static System.Console;

namespace DotNetDesignPatternDemos.SOLID.OCP
{
  public enum Color
  {
    Red, Green, Blue
  }

  public enum Size
  {
    Small, Medium, Large, Yuge
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
using static System.Console;

namespace DotNetDesignPatternDemos.SOLID.LiskovSubstitutionPrinciple
{
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
using System;

namespace DotNetDesignPatternDemos.SOLID.InterfaceSegregationPrinciple
{
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
using System;
using System.Collections.Generic;
using System.Linq;
using static System.Console;

namespace DotNetDesignPatternDemos.SOLID.DependencyInversionPrinciple
{
  // hl modules should not depend on low-level; both should depend on abstractions
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
    private List<(Person,Relationship,Person)> relations
      = new List<(Person, Relationship, Person)>();

    public void AddParentAndChild(Person parent, Person child)
    {
      relations.Add((parent, Relationship.Parent, child));
      relations.Add((child, Relationship.Child, parent));
    }

    public List<(Person, Relationship, Person)> Relations => relations;

    public IEnumerable<Person> FindAllChildrenOf(string name)
    {
      return relations
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
}
```