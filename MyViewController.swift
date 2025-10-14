import UIKit

class MyViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        self.view.backgroundColor = UIColor.systemBackground
    }

    override func loadView() {
        // Create the main view
        let view = UIView()
        view.backgroundColor = UIColor.white
        
        // Add a label as an example
        let label = UILabel()
        label.text = "Hello from MyViewController!"
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)
        
        // Add constraints for the label
        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
        
        self.view = view
    }
}