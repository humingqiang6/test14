package com.example.myapp

import android.app.Activity
import android.os.Bundle
import android.widget.Toast

class ToastActivity_9237 : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Display a toast message
        Toast.makeText(this, "Hello from Kotlin Activity!", Toast.LENGTH_SHORT).show()
    }
}