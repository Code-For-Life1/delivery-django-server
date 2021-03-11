import 'package:delivery_app/customWidgets/FancyButton.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class MerchantOrder extends StatefulWidget {
  @override
  _MerchantOrderState createState() => _MerchantOrderState();
}

class _MerchantOrderState extends State<MerchantOrder> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [],
        backgroundColor: Colors.orange[800],
        title: Text(
          'Delivery Status',
        ),
        centerTitle: true,
      ),
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