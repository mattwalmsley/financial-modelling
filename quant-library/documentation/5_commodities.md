# Commodities

- [Commodities](#commodities)
  - [Introduction](#introduction)
    - [Agriculture](#agriculture)
    - [Metals](#metals)
    - [Energy](#energy)
  - [Valuation](#valuation)
  - [Volatility](#volatility)
  - [Risks](#risks)
  - [Inventory and Storage Costs](#inventory-and-storage-costs)
    - [Convenience Yield](#convenience-yield)

## Introduction

- Commodities are primary feedstocks that have regular pricing assessment, and are usually actively traded in both the physical and derivatives markets.
- Materials can be classed as *very-specialised* feedstocks or a combination of feedstocks that have been transformed into a material.
- The 3 major types of commodity are **agriculture**, **metals** and **energy**, although other types do exist.

### Agriculture

- Crops and livestock products that are used to sustain or support life.
- **Grains** are a primary source of carbohydrate in human/livestock diets.
  - Examples include corn, wheat, barley, and rice.
- **Oilseeds** are used for food and fuel.
  - The remaining materials, once the oil has been extracted, is known as the **meal** and is used for animal feed.
  - Examples include palm, soybean, sunflower and rapeseed/canola.
  - Cotton is also classed as an oilseed but is used predominantly for its natural fibres.
- **Softs** are grown in the tropical regions.
  - Examples include coffee, sugar, cocoa, orange juice, and rubber.
- **Livestock** products which are most commonly traded are cattle and hogs.
- **Dairy** products which are most commonly traded are milk and butter, as well as some cheese.

### Metals

- **Precious metals** include gold, silver, platinum and palladium.
- **Base (industrial) metals** include copper, zinc, aluminium etc.

### Energy

- **Crude oil** is the most liquid and active commodity market worldwide.
- Other traded products include **natural gas**, **coal**, and **power**.

## Valuation

- Commodities cannot be modelled as a future stream of cash flows, unlike bonds and stocks. Discounted cash flow analysis is therefore not used for pricing commodities.
- Market forces of supply and demand determine commodity prices; however, there are identifiable trends in commodity price time series, and other market driven features relating to seasonality.

## Volatility

- Commodity prices are highly volatile based on the news and weather, but are also driven by highly speculative trading.

## Risks

- Many of the risks in other asset classes are also present in commodities - e.g. price and credit risk.
-Commodities are also exposed to a number of unique risks due to the physical nature of the asset.
- **Transportation** of the physical goods provide a risk due to the the potential for the product to be damaged or spoilt during transport, as well as the cost of the transport itself.
- The **storage** of the products also provides similar types of risk to transportation.

## Inventory and Storage Costs

- The theory of inventory has been a major advance in understanding commodity assets.
- The higher the inventory levels of a commodity, the lower the price volatility.
- Holding inventories allows both suppliers and consumers to operate with stability during a demand or supply shock.
  - Suppliers and consumers can react quickly to demand if they hold inventories.
- Generally, inventories stabilize commodities' prices, but will incur storage costs.

### Convenience Yield

- Inventories can be modelled in a similar way to dividend yields on stock, using *convenience yield*.
- Convenience yields are implemented as a continuously compounded return accruing to holdings of a commodity.
- The *net yield* accounts for the storage costs associated with holding an inventory and is modelled as a negative yield
$$Net \space Yield = Convenience \space Yield - Storage \space Costs$$
- Modelling the convenience yield $y$ and storage costs $s$ as continuously compounded, an investment of $\alpha$ units of a commodity with cost $C(t)$ would be $\alpha e^{(y - s)t}C(t)$, where $(y - s)$ represents the net yield.
- The convenience yield would never be modelled to be reinvested into the holdings of the assets.
