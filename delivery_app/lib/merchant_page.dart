import 'package:delivery_app/customWidgets/FancyButton.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class MerchantOrder2 extends StatefulWidget {
  @override
  _MerchantOrder2State createState() => _MerchantOrder2State();
}

class _MerchantOrder2State extends State<MerchantOrder2> {
  int _currentIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: Drawer(
        child: ListView(
          children: [
            DrawerHeader(child: Text('Hello')),
            ListTile(title: Text('A')),
            ListTile(title: Text('B')),
          ],
        ),
      ),
      backgroundColor: Colors.white,
    /*  appBar: AppBar(
        actions: [],
        backgroundColor: Colors.orange[800],
        title: Text(
          'Delivery Status',
        ),
        centerTitle: true,
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        backgroundColor: Colors.deepOrange,
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.drive_eta),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.delivery_dining,
            ),
            label: 'Drivers',
          )
        ],
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        selectedItemColor: Colors.amber,
      ),

     */
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        //mainAxisSize: MainAxisSize.max,
        //crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          SizedBox(),
          Center(
              child: Container(
                margin: EdgeInsets.fromLTRB(0, 270, 0, 270),
                child: Text(
                  'No orders yet',
                  style: TextStyle(fontSize: 40.0, color: Colors.orange[500]),
                ),
              )),
          Container(
            margin: EdgeInsets.fromLTRB(20, 0, 20, 0),
            child: FancyButton(
              onPressed: () {},
            ),
          ),
        ],
      ),
    );
  }
}
