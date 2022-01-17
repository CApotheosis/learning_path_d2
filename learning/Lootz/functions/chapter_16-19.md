# Scopes in python
### Scopes in functions:
- ### Names assigned inside a `def` can only be seen by the code within that `def`. You cannot even refer to such names from outside the function.
- ### Names assigned inside a def do not clash with variables outside the def, even if the same names are used elsewhere. A name `X` assigned outside a given def (i.e., in a different def or at the top level of a module file) is a completely different variable from a name `X` assigned inside that def.

<br/>

### Variable assignment rules according to scope: 
- ### If a variable is assigned inside a def, it is `local` to that function.

- ### If a variable is assigned in an enclosing `def`, it is `nonlocal` to nested functions.

- ### If a variable is assigned outside all defs, it is `global` to the entire file.

## Name Resolution: The LEGB Rule
### Three rules:
- ### Name assignments create or change local names by default.

- ### Name references search at most four scopes: local, then enclosing functions (if any), then global, then built-in.

- ### Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes, respectively.