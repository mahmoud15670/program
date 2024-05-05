import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.green),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'التسبيح بعد الصلاة'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  int _listIndex = 0;
  var mylist = ['سبحان الله','الحمد لله','لا اله الا الله','الله اكبر'];

  void _incrementCounter() {

    if (_counter == 3) {
      setState(() {
        _listIndex++;
        if (_listIndex>3) {
          _listIndex=0;
          const Placeholder();
        }
        _counter = 0;
      });
    }
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Center(child: Text(widget.title,style: Theme.of(context).textTheme.headlineLarge,)),
      ),
      body: Center(
        child: Column(

          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              mylist[_listIndex],
              style: Theme.of(context).textTheme.displayLarge,
            ),
<<<<<<< HEAD
             Card(
                color: Theme.of(context).colorScheme.inversePrimary,
                child: Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: Text(
                    '$_counter',
                    style: Theme.of(context).textTheme.headlineLarge,
                  ),
                ),
=======
            Card(
              color: Theme.of(context).colorScheme.primary,
              child: Text(
                '$_counter',
                style: Theme.of(context).textTheme.headlineLarge,
>>>>>>> 90e179b (May 2, 2024, 9:35 AM)
              ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
