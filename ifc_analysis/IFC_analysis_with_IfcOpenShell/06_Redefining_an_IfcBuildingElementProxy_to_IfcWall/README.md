# Updating the names of rooms in a model

There are many situations one would like to update information in an IFC file. One case might be the need to update information on rooms in a model.

The Rooms of a ifc model is of type IfcSpace and there are many posible ways of adding information to it both as direct attributes and in predefined or otherwise defined property sets.

As IfcSpace inherits from IfcRoot it has direct attributes of Name, Description, GlobalID and as it is aslo a IfcSpatialStructureElement it also has the attribute of LongName.

In this case we are interested in getting the Name, LongName, and GlobalID of all rooms in the model in an editable format to check and update Room Names.

So, we'll walk through

- How to get an ifc file, query its room and direct attributes of Name, LongName and GlobalID
- Write that to a csv file to handle in a 3rd party editor like eg. Google Spreadsheet, or Excel.
- Next we show how to read in this information from a csv file (separated by ",") and update the IFC model.

**Download the files above and do it yourself.**

Reference by BIMFag
