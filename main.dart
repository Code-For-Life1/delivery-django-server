import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      body: Column(
        children: [
          Center(
            child: Text("Welcome!", style: TextStyle(color: Color(0xFFFF6200), fontSize: 33)),
            heightFactor: 9,
          ),
          Center(
            child: Text("Please select a role:", style: TextStyle(color: Color(0xFFFF6200), fontSize: 22))
          ),
          Center(
            child: Container(
              width: 300,
              height: 50,
              child: RaisedButton(
                  onPressed: () {},
                  child: Text("I'm a Driver!", style: TextStyle(fontSize: 20)),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(1000),
                    side: BorderSide(color: Color(0xFFFF6200))
                  )
              )
          ),
            heightFactor: 1.93,
          ),
          Center(
            child: Container(
              width: 300,
              height: 50,
              child: RaisedButton(
                  onPressed: () {},
                  child: Text("I'm the Merchant.", style: TextStyle(fontSize: 20)),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(1000),
                    side: BorderSide(color: Color(0xFFFF6200))
                  )
              )
            )
          )
        ],
      ),
      backgroundColor: Color(0xFFF6F8F5),
    )
  ));
}