//
//  Food_TrackerTests.swift
//  Food TrackerTests
//
//  Created by Anthony Lee on 1/30/16.
//  Copyright © 2016 inSightFul inc. All rights reserved.
//

import UIKit
import XCTest
@testable import Food_Tracker

class Food_TrackerTests: XCTestCase {
    
    // FoodTracker Tests
    // Tests to confirm that the Meal Initialiser returns when no name or negative rating is provided
    func testMealInitialization() {
        
        // Success case:
        let potentialItem = Meal(name: "Newest meal", photo: nil, rating: 5)
        XCTAssertNotNil(potentialItem)
        
        // Failure cases:
        let noName = Meal(name: "", photo: nil, rating: 0)
        XCTAssertNil(noName, "Empty name is invalid")
        
        let badRating = Meal(name: "Really bad rating", photo: nil, rating: -1)
        XCTAssertNil(badRating, "Negative ratings are invalid, be positive")
        
    }
    
//    override func setUp() {
//        super.setUp()
//        // Put setup code here. This method is called before the invocation of each test method in the class.
//    }
//    
//    override func tearDown() {
//        // Put teardown code here. This method is called after the invocation of each test method in the class.
//        super.tearDown()
//    }
//    
//    func testExample() {
//        // This is an example of a functional test case.
//        // Use XCTAssert and related functions to verify your tests produce the correct results.
//    }
//    
//    func testPerformanceExample() {
//        // This is an example of a performance test case.
//        self.measureBlock {
//            // Put the code you want to measure the time of here.
//        }
//    }
    
}
