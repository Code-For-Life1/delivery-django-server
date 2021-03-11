import 'package:flutter/material.dart';



// Driver: full name, phone number, address.
class DriverAdd extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double screenSize = MediaQuery.of(context).size.width;
    return Scaffold(
      appBar: AppBar(
        leadingWidth: 56 * 2.0,
        leading: Center(
          child: FlatButton(
            onPressed: () => Navigator.pop(context),
            child: Text(
              "Cancel",
              style: TextStyle(
                fontSize: 20,
                color: Colors.white,
              ),
            ),
          ),
        ),
        actions: [
          Center(
            child: FlatButton(
              onPressed: () => {},
              child: Text(
                "Done",
                style: TextStyle(
                  fontSize: 20,
                  color: Colors.white,
                ),
              ),
            ),
          ),
        ],
        automaticallyImplyLeading: false,
        title: Text(
          "Add Driver",
          style: TextStyle(color: Colors.white, fontSize: 23),
        ),
        centerTitle: true,
        backgroundColor: Color(0xFFFF6200),
        toolbarHeight: 53,
      ),
      body: Container(
          transform: Matrix4.translationValues(0.0, (screenSize * 0.15), 0.0),
          child: Center(
              child: Column(children: [
                Image(
                  height: screenSize * 0.2,
                  image: AssetImage("assets/portrait.png"),
                ),
                Container(
                    margin: EdgeInsets.only(top: screenSize * 0.06),
                    child: new Wrap(
                      direction: Axis.horizontal,
                      crossAxisAlignment: WrapCrossAlignment.start,
                      spacing: screenSize * 0.05,
                      runSpacing: 15,
                      children: [
                        Container(
                          width: screenSize * 0.4,
                          child: TextField(
                            style: TextStyle(fontSize: 22),
                            decoration: new InputDecoration(
                              fillColor: Color(0xFFF8F8F8),
                              filled: true,
                              contentPadding: EdgeInsets.only(left: 7.0),
                              hintText: 'First name',
                              border: new OutlineInputBorder(
                                borderRadius: const BorderRadius.all(
                                  const Radius.circular(10.0),
                                ),
                              ),
                            ),
                          ),
                        ),
                        Container(
                          width: screenSize * 0.4,
                          child: TextField(
                            style: TextStyle(fontSize: 22),
                            decoration: new InputDecoration(
                              fillColor: Color(0xFFF8F8F8),
                              filled: true,
                              contentPadding: EdgeInsets.only(left: 7.0),
                              hintText: 'Last name',
                              border: new OutlineInputBorder(
                                borderRadius: const BorderRadius.all(
                                  const Radius.circular(10.0),
                                ),
                              ),
                            ),
                          ),
                        ),
                        Container(
                          width: screenSize * 0.85,
                          child: TextField(
                            style: TextStyle(fontSize: 22),
                            decoration: new InputDecoration(
                              fillColor: Color(0xFFF8F8F8),
                              filled: true,
                              contentPadding: EdgeInsets.only(left: 15.0),
                              hintText: 'Home address',
                              border: new OutlineInputBorder(
                                borderRadius: const BorderRadius.all(
                                  const Radius.circular(10.0),
                                ),
                              ),
                            ),
                          ),
                        ),
                        Container(
                            width: screenSize * 0.85,
                            child: TextField(
                              style: TextStyle(fontSize: 22),
                              decoration: new InputDecoration(
                                fillColor: Color(0xFFF8F8F8),
                                filled: true,
                                contentPadding: EdgeInsets.only(left: 15.0),
                                hintText: 'Phone number',
                                border: new OutlineInputBorder(
                                  borderRadius: const BorderRadius.all(
                                    const Radius.circular(10.0),
                                  ),
                                ),
                              ),
                            ))
                      ],
                    )),
                Container(
                  margin: EdgeInsets.only(
                    top: screenSize * 0.5,
                  ),
                )
              ]))),
      backgroundColor: Color(0xFFF6F8F5),
    );
  }
}


/*
class DriverSignUp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(

    );
  }
}

 */