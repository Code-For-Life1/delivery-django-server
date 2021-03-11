import 'package:flutter/material.dart';

class DriverSignUp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.orange[800],
        title: Text('Driver Sign up'),
        centerTitle: true,
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
              'Enter your token',
            style: TextStyle(
              fontSize: 25
            ),
          ),
          SizedBox(height: 10),
          Container(
            margin: EdgeInsets.fromLTRB(20, 0, 20, 0),
            child: TextField(
              style: TextStyle(fontSize: 16),
              decoration: new InputDecoration(
                fillColor: Color(0xFFF8F8F8),
                filled: true,
                contentPadding: EdgeInsets.fromLTRB(20, 0, 20, 0),
                hintText: 'e.g: yj18N3JiVJtu0lPob7BFs4MlHXBGREhh',
                border: new OutlineInputBorder(
                  borderRadius: const BorderRadius.all(
                    const Radius.circular(10.0),
                  ),
                ),
              ),

            ),
          ),
          SizedBox(height: 20),
          TextButton(
            onPressed: (){},
            child: Text('Validate'),
          )
        ],
      ),
    );
  }
}
