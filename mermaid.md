```
flowchart TD
    Bonus{"H.C. > Bonus?"} -->|No| Draw
    Bonus -->|Yes| Decrement
    Decrement[Decrement H.C.]
    Draw(Draw 2) --> Decrement
    Decrement --> Initiative{Initiative?}
    Initiative -->|Yes| ClearSeize[Remove Seize Counter]
    ClearSeize --> Event{Event?}
    Initiative -->|No| Surpass{Surpass?}
    Surpass -->|Yes| SelectSurpass["`Select card to surpass.
                                     Prefer: higher number`"]
    Surpass -->|No| CheckSeize["`Check for seize.
                                 Go to General Priorities`"]
    Event -->|Yes| DrawNonEvents[Draw until 2 non-Events. Shuffle Events back]
    DrawNonEvents --> Ambition
    Event -->|No| Ambition{Ambition?}
    Ambition -->|Yes| Declare
```