import 'package:flutter/material.dart';

class MerchantDrivers extends StatefulWidget {
  @override
  _MerchantDriversState createState() => _MerchantDriversState();
}

class _MerchantDriversState extends State<MerchantDrivers> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView.builder(
        itemCount: 20,
        itemBuilder: (context,index){
          return Card(
            color: Colors.amber,
            child: Column(
              children: [
                Text('Driver${index+1}'),
                Text('Name: Mahmoud'),
                Text('Hello3')
              ],
            ),
          );
        }
      )
    );
  }
}
