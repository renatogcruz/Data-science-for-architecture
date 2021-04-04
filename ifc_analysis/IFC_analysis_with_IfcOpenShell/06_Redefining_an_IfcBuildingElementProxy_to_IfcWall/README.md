# How to change from a IfcBuildingElementProxy to IfcWall

Here is some code that changes all elements of type IfcBuildingElementProxy, to an element of IfcWall.

First we create a helper function to add an object to the list of objects that a relationship object refer to. This is used to add the new object when we remove the old i.e. add the inverse attributes to the new object.

Second we create a function that takes in a path to a file, and a path to a new file, that will change all elements of type IfcWall to IfcProduct.

An underlying assumption in this script is that the particular IfcBuildingElementProxy elements are actually walls, only exported with a more abstract entity.

- Getting all elements of IfcBuildingElementProxy from the file
- Iterating through all elements one by one and storing a reference to all direct and iverse attributes
- Creating a new instance of IfcWall with the direct attributes of the IfcBuildingElementProxy object.
- Removing the old IfcBuildingElementProxy object
- Iterating through all inverse attributes (holding a relational object) and adding the new IfcWall to the relational object.
- Store the new file.

A reference to do this type of script is the [creating a simple wall with property set and quantity set on the ifcopenshell academy](http://academy.ifcopenshell.org/creating-a-simple-wall-with-property-set-and-quantity-information/)

**Download the files above and do it yourself.**

Reference by BIMFag
