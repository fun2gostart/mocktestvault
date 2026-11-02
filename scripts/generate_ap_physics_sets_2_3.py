#!/usr/bin/env python3
"""
Generates AP Physics 1 Sets 02 & 03 (40 Questions total):
- ap_physics_1_set2.json (Unit 2: Dynamics & Newton's Laws)
- ap_physics_1_set3.json (Unit 3 & 4: Circular Motion, Gravitation & Work-Energy)
"""

import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_AP = os.path.join(BASE_DIR, "data", "us", "ap")
os.makedirs(US_DATA_AP, exist_ok=True)

# ==============================================================================
# SET 02: DYNAMICS & NEWTON'S LAWS OF MOTION (20 Questions - Unit 2)
# ==============================================================================
ap_phys_set2 = [
  {
    "id": "ap-phys-021",
    "type": "mcq",
    "subtopic": "Static vs Kinetic Friction (Unit 2)",
    "difficulty": "Medium",
    "question": "A 10 kg crate rests on a horizontal wooden floor. The coefficient of static friction is μs = 0.5 and kinetic friction is μk = 0.3. A horizontal force of 40 N is applied to the crate. What is the magnitude of the friction force acting on the crate? (Use g = 10 m/s^2)",
    "options": ["40 N", "50 N", "30 N", "0 N"],
    "answer": 0,
    "explanation": "Normal force F_N = mg = 10 kg * 10 m/s^2 = 100 N. Maximum static friction f_s,max = μs * F_N = 0.5 * 100 N = 50 N. Because the applied force of 40 N is less than 50 N, the crate does not move (a = 0). By Newton's First Law, static friction exactly balances the applied force: f_s = 40 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.5 Friction and Newton's Second Law"
  },
  {
    "id": "ap-phys-022",
    "type": "mcq",
    "subtopic": "Inclined Plane with Friction (Unit 2)",
    "difficulty": "Medium",
    "question": "A block of mass m slides down an incline tilted at angle θ above the horizontal at a constant velocity. What is the coefficient of kinetic friction μk between the block and the incline?",
    "options": ["tan(θ)", "sin(θ)", "cos(θ)", "1 / tan(θ)"],
    "answer": 0,
    "explanation": "At constant velocity, acceleration a = 0. Forces parallel to incline: mg * sin(θ) - f_k = 0 → f_k = mg * sin(θ). Normal force F_N = mg * cos(θ). Since f_k = μk * F_N: μk * mg * cos(θ) = mg * sin(θ) → μk = sin(θ) / cos(θ) = tan(θ).",
    "citation": "College Board AP® Physics 1 CED — Topic 2.6 Inclined Planes"
  },
  {
    "id": "ap-phys-023",
    "type": "mcq",
    "subtopic": "Atwood Machine Acceleration (Unit 2)",
    "difficulty": "Medium",
    "question": "An ideal Atwood machine consists of two masses m1 = 3 kg and m2 = 5 kg connected by a light string over a frictionless, massless pulley. What is the acceleration of the system? (Use g = 9.8 m/s^2)",
    "options": ["2.45 m/s^2", "4.90 m/s^2", "1.23 m/s^2", "9.80 m/s^2"],
    "answer": 0,
    "explanation": "System acceleration a = (m2 - m1) * g / (m1 + m2) = (5 - 3) * 9.8 / (5 + 3) = 2 * 9.8 / 8 = 19.6 / 8 = 2.45 m/s^2.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.7 Two-Body Systems and Connected Objects"
  },
  {
    "id": "ap-phys-024",
    "type": "mcq",
    "subtopic": "Atwood Machine String Tension (Unit 2)",
    "difficulty": "Hard",
    "question": "For the Atwood machine in the previous problem (m1 = 3 kg, m2 = 5 kg, g = 9.8 m/s^2, a = 2.45 m/s^2), what is the tension in the connecting string?",
    "options": ["36.75 N", "49.0 N", "29.4 N", "19.6 N"],
    "answer": 0,
    "explanation": "Consider the lighter mass m1 accelerating upward: T - m1*g = m1*a → T = m1(g + a) = 3 kg * (9.8 + 2.45) m/s^2 = 3 * 12.25 = 36.75 N. (Check with m2: m2*g - T = m2*a → T = 5(9.8 - 2.45) = 5(7.35) = 36.75 N).",
    "citation": "College Board AP® Physics 1 CED — Topic 2.7 Two-Body Systems and Connected Objects"
  },
  {
    "id": "ap-phys-025",
    "type": "mcq",
    "subtopic": "Apparent Weight in an Elevator (Unit 2)",
    "difficulty": "Medium",
    "question": "A 60 kg student stands on a scale in an elevator. What does the scale read, in Newtons, when the elevator accelerates upward at 2.5 m/s^2? (Use g = 9.8 m/s^2)",
    "options": ["738 N", "588 N", "438 N", "150 N"],
    "answer": 0,
    "explanation": "The scale measures normal force F_N. Applying Newton's Second Law: F_N - mg = ma → F_N = m(g + a) = 60 kg * (9.8 + 2.5) m/s^2 = 60 * 12.3 = 738 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.2 Newton's First and Second Laws"
  },
  {
    "id": "ap-phys-026",
    "type": "mcq",
    "subtopic": "Newton's Third Law Action-Reaction (Unit 2)",
    "difficulty": "Easy",
    "question": "A heavy transport truck collides head-on with a small compact car. During the collision, how does the magnitude of the force exerted by the truck on the car compare to the magnitude of the force exerted by the car on the truck?",
    "options": [
      "The forces are strictly equal in magnitude according to Newton's Third Law",
      "The truck exerts a greater force because of its much larger mass",
      "The car exerts a greater force because it experiences a larger acceleration",
      "The force of the truck depends on its initial velocity prior to impact"
    ],
    "answer": 0,
    "explanation": "According to Newton's Third Law, every action has an equal and opposite reaction. The contact force exerted by the truck on the car is strictly equal in magnitude and opposite in direction to the force exerted by the car on the truck, regardless of their masses or accelerations.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.3 Newton's Third Law and Free-Body Diagrams"
  },
  {
    "id": "ap-phys-027",
    "type": "mcq",
    "subtopic": "Tabletop Modified Atwood System (Unit 2)",
    "difficulty": "Hard",
    "question": "A 4 kg block rests on a frictionless horizontal table and is attached to a 1 kg hanging mass by a light cord over a frictionless pulley. What is the acceleration of the 4 kg block? (Use g = 10 m/s^2)",
    "options": ["2.0 m/s^2", "2.5 m/s^2", "10.0 m/s^2", "8.0 m/s^2"],
    "answer": 0,
    "explanation": "The net external pulling force on the total system is the weight of the hanging mass: F_net = m_hang * g = 1 kg * 10 m/s^2 = 10 N. Total system mass = m_table + m_hang = 4 kg + 1 kg = 5 kg. a = F_net / m_total = 10 N / 5 kg = 2.0 m/s^2.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.7 Two-Body Systems"
  },
  {
    "id": "ap-phys-028",
    "type": "mcq",
    "subtopic": "Pushed Stacks of Blocks (Unit 2)",
    "difficulty": "Medium",
    "question": "Two blocks, A (mass 6 kg) and B (mass 4 kg), sit in contact on a frictionless surface. A horizontal force F = 30 N pushes block A toward block B. What is the magnitude of the contact force that block A exerts on block B?",
    "options": ["12 N", "18 N", "30 N", "6 N"],
    "answer": 0,
    "explanation": "Total system acceleration a = F / (m_A + m_B) = 30 N / (6 + 4) kg = 3.0 m/s^2. Block B is accelerated purely by the contact force F_AB: F_AB = m_B * a = 4 kg * 3.0 m/s^2 = 12 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.2 Newton's Second Law and Systems"
  },
  {
    "id": "ap-phys-029",
    "type": "mcq",
    "subtopic": "Pulling at an Angle with Friction (Unit 2)",
    "difficulty": "Hard",
    "question": "A sled of mass 20 kg is pulled across level snow by a rope with tension T = 50 N directed at an angle of 37° above the horizontal (cos 37° ≈ 0.8, sin 37° ≈ 0.6). What is the normal force exerted by the snow on the sled? (Use g = 10 m/s^2)",
    "options": ["170 N", "200 N", "230 N", "160 N"],
    "answer": 0,
    "explanation": "Vertical forces: F_N + T*sin(37°) - mg = 0. T*sin(37°) = 50 * 0.6 = 30 N. mg = 20 * 10 = 200 N. F_N = 200 N - 30 N = 170 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.1 Systems and Free-Body Diagrams"
  },
  {
    "id": "ap-phys-030",
    "type": "mcq",
    "subtopic": "Terminal Velocity & Drag (Unit 2)",
    "difficulty": "Medium",
    "question": "An object of mass m falls through air where air resistance is modeled by F_drag = b*v. What is the terminal velocity of the falling object?",
    "options": ["mg / b", "b / (mg)", "√(mg / b)", "m / (bg)"],
    "answer": 0,
    "explanation": "At terminal velocity, the net force is zero and acceleration a = 0. mg - F_drag = 0 → mg - b*v_term = 0 → v_term = mg / b.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.2 Forces and Terminal Velocity"
  },
  {
    "id": "ap-phys-031",
    "type": "mcq",
    "subtopic": "Free-Body Diagram Verification (Unit 2)",
    "difficulty": "Easy",
    "question": "A book is at rest on a horizontal tabletop. What forces act on the book?",
    "options": [
      "Downward gravitational force by Earth and upward normal force by the table",
      "Downward gravitational force and upward force of inertia",
      "Downward gravitational force, upward normal force, and forward static friction",
      "Only the downward gravitational force"
    ],
    "answer": 0,
    "explanation": "A stationary book on a level table experiences exactly two contact and field forces: the downward gravitational pull from Earth and the perpendicular upward normal force from the table. There are no horizontal applied forces, so friction is zero.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.1 Free-Body Diagrams"
  },
  {
    "id": "ap-phys-032",
    "type": "mcq",
    "subtopic": "Two Hanging Masses on Vertical String (Unit 2)",
    "difficulty": "Medium",
    "question": "Mass A (2 kg) hangs by a string from the ceiling. Mass B (3 kg) hangs by a second string from the bottom of Mass A. What is the tension in the string connecting Mass A to the ceiling? (Use g = 9.8 m/s^2)",
    "options": ["49.0 N", "29.4 N", "19.6 N", "9.8 N"],
    "answer": 0,
    "explanation": "The top string supports both masses (m_total = 2 + 3 = 5 kg). In static equilibrium: T_top = m_total * g = 5 kg * 9.8 m/s^2 = 49.0 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.2 Equilibrium Systems"
  },
  {
    "id": "ap-phys-033",
    "type": "mcq",
    "subtopic": "Apparent Weight in Free Fall (Unit 2)",
    "difficulty": "Easy",
    "question": "If the elevator cable snaps and the elevator falls freely with downward acceleration g, what does the bathroom scale under a passenger read?",
    "options": ["0 N", "mg", "2mg", "-mg"],
    "answer": 0,
    "explanation": "In free fall, a = g downward. Equation: mg - F_N = ma → mg - F_N = mg → F_N = 0 N. The passenger experiences apparent weightlessness.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.2 Apparent Weight and Free Fall"
  },
  {
    "id": "ap-phys-034",
    "type": "mcq",
    "subtopic": "Horizontal Acceleration of Incline (Unit 2)",
    "difficulty": "Hard",
    "question": "A frictionless wedge of angle θ is accelerated horizontally with acceleration a such that a small block resting on the incline does not slide up or down. What must acceleration a equal?",
    "options": ["g * tan(θ)", "g * sin(θ)", "g * cos(θ)", "g / tan(θ)"],
    "answer": 0,
    "explanation": "The normal force F_N has vertical component F_N * cos(θ) = mg and horizontal component F_N * sin(θ) = ma. Divide the horizontal equation by the vertical equation: tan(θ) = ma / mg = a / g → a = g * tan(θ).",
    "citation": "College Board AP® Physics 1 CED — Topic 2.6 Inclined Planes in Non-Inertial/Accelerating Frames"
  },
  {
    "id": "ap-phys-035",
    "type": "mcq",
    "subtopic": "Deceleration by Friction (Unit 2)",
    "difficulty": "Medium",
    "question": "A car travelling on a flat road at speed v0 slams on its brakes and skids to a stop with locked wheels. If the coefficient of kinetic friction is μk, which expression gives the stopping distance d?",
    "options": ["v0^2 / (2 * μk * g)", "v0^2 / (μk * g)", "2 * v0^2 / (μk * g)", "v0 / (μk * g)"],
    "answer": 0,
    "explanation": "Frictional deceleration a = f_k / m = (μk * mg) / m = μk * g. Using kinematics v^2 = v0^2 - 2ad with final v = 0: 0 = v0^2 - 2(μk * g)d → d = v0^2 / (2 * μk * g).",
    "citation": "College Board AP® Physics 1 CED — Topic 2.5 Friction and Kinematics"
  },
  {
    "id": "ap-phys-036",
    "type": "mcq",
    "subtopic": "String Tension for Mass on Frictionless Incline (Unit 2)",
    "difficulty": "Medium",
    "question": "A 5 kg block is held stationary on a frictionless 30° incline by a rope parallel to the incline. What is the tension in the rope? (Use g = 9.8 m/s^2)",
    "options": ["24.5 N", "49.0 N", "42.4 N", "12.25 N"],
    "answer": 0,
    "explanation": "For equilibrium parallel to the incline: T = mg * sin(θ) = 5 kg * 9.8 m/s^2 * sin(30°) = 49 * 0.5 = 24.5 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.6 Inclined Planes"
  },
  {
    "id": "ap-phys-037",
    "type": "mcq",
    "subtopic": "Kinetic Friction Work and Heat (Unit 2)",
    "difficulty": "Easy",
    "question": "Which of the following statements about the force of kinetic friction is always true?",
    "options": [
      "It acts parallel to the contact surfaces in a direction opposite to the relative sliding motion",
      "It is directly proportional to the apparent surface area of contact",
      "It increases linearly as the relative sliding speed increases",
      "It is always strictly greater than static friction for the same surfaces"
    ],
    "answer": 0,
    "explanation": "Kinetic friction always opposes the relative sliding motion between two contacting surfaces and is directed parallel to the contact interface.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.5 Friction"
  },
  {
    "id": "ap-phys-038",
    "type": "mcq",
    "subtopic": "Multi-Mass System with Different Incline Angles (Unit 2)",
    "difficulty": "Hard",
    "question": "Two masses m1 = 4 kg and m2 = 4 kg sit on a double frictionless ramp. m1 is on a 30° slope and m2 is on a 60° slope, connected by a light string over the peak pulley. Which way will the system accelerate?",
    "options": [
      "m2 accelerates down the 60° slope because mg*sin(60°) > mg*sin(30°)",
      "m1 accelerates down the 30° slope because it has greater mechanical advantage",
      "The system remains in static equilibrium because both masses are 4 kg",
      "The system oscillates back and forth perpetually"
    ],
    "answer": 0,
    "explanation": "The gravitational force pulling parallel to the slope on m2 is m2*g*sin(60°) = 4g * 0.866 = 3.464g. For m1, m1*g*sin(30°) = 4g * 0.5 = 2.0g. Because 3.464g > 2.0g, m2 accelerates down the 60° slope.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.7 Two-Body Systems on Inclines"
  },
  {
    "id": "ap-phys-039",
    "type": "mcq",
    "subtopic": "Newton's Second Law with Variable Mass/Rocket Analogy (Unit 2)",
    "difficulty": "Medium",
    "question": "A constant net horizontal force F is applied to a cart. As the cart moves, sand leaks out of a hole in the bottom of the cart at a steady rate. What happens to the acceleration of the cart?",
    "options": [
      "The acceleration increases continuously because the total mass decreases",
      "The acceleration remains constant because force F is constant",
      "The acceleration decreases because momentum is carried away by the sand",
      "The acceleration drops to zero"
    ],
    "answer": 0,
    "explanation": "By Newton's Second Law, a = F_net / m. If the net force F_net is held constant while mass m decreases due to leaking sand, the denominator decreases, causing acceleration a to increase continuously.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.2 Newton's Second Law"
  },
  {
    "id": "ap-phys-040",
    "type": "mcq",
    "subtopic": "Scale Force on Accelerating Frame (Unit 2)",
    "difficulty": "Medium",
    "question": "An elevator accelerates downward at a rate of a = 2.0 m/s^2. If a passenger has a mass of 50 kg, what is the normal force exerted on the passenger? (Use g = 9.8 m/s^2)",
    "options": ["390 N", "490 N", "590 N", "100 N"],
    "answer": 0,
    "explanation": "Downward acceleration: mg - F_N = ma → F_N = m(g - a) = 50 kg * (9.8 - 2.0) m/s^2 = 50 * 7.8 = 390 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 2.2 Apparent Weight"
  }
]

# Write AP Physics Set 2
with open(os.path.join(US_DATA_AP, "ap_physics_1_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ap_phys_set2}, f, indent=2, ensure_ascii=False)
print("Generated ap_physics_1_set2.json (20 Qs)!")

# ==============================================================================
# SET 03: CIRCULAR MOTION, GRAVITATION & WORK-ENERGY (20 Questions - Units 3 & 4)
# ==============================================================================
ap_phys_set3 = [
  {
    "id": "ap-phys-041",
    "type": "mcq",
    "subtopic": "Centripetal Acceleration and Speed (Unit 3)",
    "difficulty": "Easy",
    "question": "A race car travels around a flat circular track of radius 200 meters at a constant speed of 40 m/s. What is the magnitude of the car's centripetal acceleration?",
    "options": ["8.0 m/s^2", "0.2 m/s^2", "16.0 m/s^2", "4.0 m/s^2"],
    "answer": 0,
    "explanation": "Centripetal acceleration a_c = v^2 / r = (40 m/s)^2 / 200 m = 1600 / 200 = 8.0 m/s^2.",
    "citation": "College Board AP® Physics 1 CED — Topic 3.1 Centripetal Acceleration and Centripetal Force"
  },
  {
    "id": "ap-phys-042",
    "type": "mcq",
    "subtopic": "Maximum Speed on Unbanked Curve (Unit 3)",
    "difficulty": "Medium",
    "question": "A car rounds an unbanked circular curve of radius r on a level road with static coefficient of friction μs. What is the maximum speed the car can achieve without skidding outward?",
    "options": ["√(μs * g * r)", "μs * g * r", "√(g * r / μs)", "2 * √(μs * g * r)"],
    "answer": 0,
    "explanation": "Centripetal force is provided entirely by static friction: f_s,max = m*v^2 / r → μs * m * g = m * v^2 / r → v^2 = μs * g * r → v_max = √(μs * g * r).",
    "citation": "College Board AP® Physics 1 CED — Topic 3.2 Centripetal Force and Friction"
  },
  {
    "id": "ap-phys-043",
    "type": "mcq",
    "subtopic": "Newton's Law of Universal Gravitation (Unit 3)",
    "difficulty": "Easy",
    "question": "If the distance between two spherical masses in deep space is doubled, what happens to the magnitude of the gravitational attraction between them?",
    "options": [
      "It decreases to 1/4 of its original value",
      "It decreases to 1/2 of its original value",
      "It remains constant",
      "It quadruples"
    ],
    "answer": 0,
    "explanation": "Newton's Law of Universal Gravitation: F_g = G * m1 * m2 / r^2. Since gravitational force is inversely proportional to the square of the distance (1/r^2), doubling r multiplies the force by 1/(2^2) = 1/4.",
    "citation": "College Board AP® Physics 1 CED — Topic 3.3 Gravitational Fields and Universal Gravitation"
  },
  {
    "id": "ap-phys-044",
    "type": "mcq",
    "subtopic": "Orbital Speed of a Satellite (Unit 3)",
    "difficulty": "Medium",
    "question": "A satellite of mass m orbits Earth (mass M_E) in a circular orbit of radius r. What is the orbital speed of the satellite?",
    "options": ["√(G * M_E / r)", "G * M_E / r^2", "√(2 * G * M_E / r)", "√(G * m / r)"],
    "answer": 0,
    "explanation": "Centripetal force is provided by gravity: G * M_E * m / r^2 = m * v^2 / r → v^2 = G * M_E / r → v = √(G * M_E / r). Note orbital speed is independent of the satellite's mass m.",
    "citation": "College Board AP® Physics 1 CED — Topic 3.3 Orbits and Kepler's Third Law"
  },
  {
    "id": "ap-phys-045",
    "type": "mcq",
    "subtopic": "Work Done by Constant Force at an Angle (Unit 4)",
    "difficulty": "Easy",
    "question": "A worker pulls a crate a distance of 10 meters across a smooth warehouse floor using a rope with tension 60 N inclined at 60° above the horizontal. How much work is done by the rope?",
    "options": ["300 J", "600 J", "520 J", "0 J"],
    "answer": 0,
    "explanation": "Work W = F * d * cos(θ) = 60 N * 10 m * cos(60°) = 600 * 0.5 = 300 J.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.1 Work and Mechanical Energy"
  },
  {
    "id": "ap-phys-046",
    "type": "mcq",
    "subtopic": "Work Done by Normal Force on Level Ground (Unit 4)",
    "difficulty": "Easy",
    "question": "A 50 kg trunk slides horizontally across a level floor for 8 meters. What is the work done by the normal force on the trunk?",
    "options": ["0 J", "3,920 J", "400 J", "-3,920 J"],
    "answer": 0,
    "explanation": "The normal force acts vertically upward (θ = 90° relative to horizontal displacement). Work W = F_N * d * cos(90°) = 0 J. Forces perpendicular to displacement do zero work.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.1 Work"
  },
  {
    "id": "ap-phys-047",
    "type": "mcq",
    "subtopic": "Work-Energy Theorem (Unit 4)",
    "difficulty": "Medium",
    "question": "A 2 kg cart has initial kinetic energy of 25 J. A net force does 75 J of work on the cart. What is the final speed of the cart?",
    "options": ["10 m/s", "5 m/s", "7.07 m/s", "14.1 m/s"],
    "answer": 0,
    "explanation": "Work-Energy Theorem: W_net = ΔK = K_f - K_i → 75 J = K_f - 25 J → K_f = 100 J. Kinetic energy K_f = (1/2) * m * v_f^2 → 100 = (1/2)(2) * v_f^2 = v_f^2 → v_f = √100 = 10 m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.2 Work-Energy Theorem"
  },
  {
    "id": "ap-phys-048",
    "type": "mcq",
    "subtopic": "Elastic Potential Energy of Spring (Unit 4)",
    "difficulty": "Medium",
    "question": "A spring with spring constant k = 400 N/m is compressed by 0.15 m from its equilibrium length. How much elastic potential energy is stored in the spring?",
    "options": ["4.5 J", "9.0 J", "30.0 J", "60.0 J"],
    "answer": 0,
    "explanation": "Elastic potential energy U_s = (1/2) * k * x^2 = 0.5 * 400 N/m * (0.15 m)^2 = 200 * 0.0225 = 4.5 J.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.2 Potential Energy and Conservation"
  },
  {
    "id": "ap-phys-049",
    "type": "mcq",
    "subtopic": "Conservation of Mechanical Energy: Roller Coaster (Unit 4)",
    "difficulty": "Medium",
    "question": "A roller coaster cart of mass m starts from rest at the top of a hill of height h = 45 meters. Neglecting friction and air resistance, what is the speed of the cart at the bottom of the hill? (Use g = 10 m/s^2)",
    "options": ["30 m/s", "45 m/s", "21.2 m/s", "15 m/s"],
    "answer": 0,
    "explanation": "Conservation of mechanical energy: mgh = (1/2)mv^2 → v = √(2gh) = √(2 * 10 m/s^2 * 45 m) = √900 = 30 m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.3 Conservation of Energy"
  },
  {
    "id": "ap-phys-050",
    "type": "mcq",
    "subtopic": "Banked Turn Without Friction (Unit 3)",
    "difficulty": "Hard",
    "question": "An engineer designs an icy (frictionless) road turn with radius r = 100 m banked at angle θ = 45°. At what design speed can cars safely negotiate the curve? (Use g = 9.8 m/s^2, tan 45° = 1.0)",
    "options": ["31.3 m/s", "980 m/s", "22.1 m/s", "14.0 m/s"],
    "answer": 0,
    "explanation": "On a frictionless banked turn: F_N * sin(θ) = mv^2/r and F_N * cos(θ) = mg. Dividing yields tan(θ) = v^2 / (rg) → v = √(r * g * tan(θ)) = √(100 * 9.8 * 1) = √980 ≈ 31.3 m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 3.2 Banked Curves"
  },
  {
    "id": "ap-phys-051",
    "type": "mcq",
    "subtopic": "Work Done by Variable Force (Area Under F-x Graph) (Unit 4)",
    "difficulty": "Medium",
    "question": "A force parallel to the x-axis acts on a particle. The force increases linearly from F = 0 N at x = 0 m to F = 20 N at x = 4 m. How much work is done on the particle between x = 0 and x = 4 m?",
    "options": ["40 J", "80 J", "20 J", "10 J"],
    "answer": 0,
    "explanation": "Work is the area under the F vs x graph. The area is a triangle with base 4 m and height 20 N: Area = (1/2) * base * height = (1/2) * 4 m * 20 N = 40 J.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.1 Work Calculated from Force-Displacement Graphs"
  },
  {
    "id": "ap-phys-052",
    "type": "mcq",
    "subtopic": "Mechanical Power Calculation (Unit 4)",
    "difficulty": "Easy",
    "question": "An electric crane lifts a 500 kg steel beam vertically upward at a constant speed of 2.0 m/s. What mechanical power is delivered by the crane? (Use g = 9.8 m/s^2)",
    "options": ["9,800 W", "4,900 W", "1,000 W", "19,600 W"],
    "answer": 0,
    "explanation": "At constant speed, lifting force equals weight: F = mg = 500 * 9.8 = 4,900 N. Power P = F * v = 4,900 N * 2.0 m/s = 9,800 W (or 9.8 kW).",
    "citation": "College Board AP® Physics 1 CED — Topic 4.4 Power"
  },
  {
    "id": "ap-phys-053",
    "type": "mcq",
    "subtopic": "Vertical Circular Motion Minimum Speed at Top (Unit 3)",
    "difficulty": "Hard",
    "question": "A bucket of water of mass m is swung in a vertical circle of radius R. What is the minimum speed v_top at the highest point of the loop required for the water to stay in the bucket without falling out?",
    "options": ["√(g * R)", "√(2 * g * R)", "g * R", "2 * √(g * R)"],
    "answer": 0,
    "explanation": "At the top of the vertical loop: F_N + mg = m * v^2 / R. For the water to barely stay in contact, the normal force F_N approaches 0. Thus mg = m * v_top^2 / R → v_top = √(g * R).",
    "citation": "College Board AP® Physics 1 CED — Topic 3.2 Vertical Circular Motion"
  },
  {
    "id": "ap-phys-054",
    "type": "mcq",
    "subtopic": "Gravitational Acceleration at Altitude (Unit 3)",
    "difficulty": "Medium",
    "question": "Earth has radius R_E. At an altitude h = R_E above Earth's surface (distance 2R_E from Earth's center), what is the acceleration due to gravity compared to surface gravity g?",
    "options": ["g / 4", "g / 2", "g / 8", "g"],
    "answer": 0,
    "explanation": "Gravitational acceleration g(r) = G * M_E / r^2. At distance r = 2R_E, g(2R_E) = G * M_E / (2R_E)^2 = (G * M_E / R_E^2) / 4 = g / 4.",
    "citation": "College Board AP® Physics 1 CED — Topic 3.3 Gravitational Fields"
  },
  {
    "id": "ap-phys-055",
    "type": "mcq",
    "subtopic": "Mechanical Energy with Friction Dissipation (Unit 4)",
    "difficulty": "Hard",
    "question": "A 2 kg block slides down a rough incline from a height of 5 meters. Its speed at the bottom is 8 m/s. How much mechanical energy was dissipated into thermal energy by friction? (Use g = 10 m/s^2)",
    "options": ["36 J", "64 J", "100 J", "18 J"],
    "answer": 0,
    "explanation": "Initial mechanical energy E_i = mgh = 2 kg * 10 m/s^2 * 5 m = 100 J. Final mechanical energy E_f = (1/2)mv^2 = 0.5 * 2 kg * (8 m/s)^2 = 64 J. Energy dissipated = E_i - E_f = 100 J - 64 J = 36 J.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.3 Conservation of Energy with Non-Conservative Forces"
  },
  {
    "id": "ap-phys-056",
    "type": "mcq",
    "subtopic": "Kepler's Third Law Ratio (Unit 3)",
    "difficulty": "Medium",
    "question": "Satellite A orbits a planet at orbital radius r with period T. Satellite B orbits the same planet at orbital radius 4r. What is the orbital period of Satellite B?",
    "options": ["8T", "4T", "16T", "2T"],
    "answer": 0,
    "explanation": "By Kepler's Third Law: T^2 ∝ r^3 → T_B / T_A = (r_B / r_A)^(3/2) = (4)^(3/2) = (√4)^3 = 2^3 = 8. Thus T_B = 8T.",
    "citation": "College Board AP® Physics 1 CED — Topic 3.3 Kepler's Laws and Planetary Motion"
  },
  {
    "id": "ap-phys-057",
    "type": "mcq",
    "subtopic": "Tension in Simple Pendulum at Bottom (Unit 4)",
    "difficulty": "Hard",
    "question": "A simple pendulum consists of a bob of mass m on a string of length L. The bob is released from rest from a horizontal position (angle 90°). What is the tension in the string at the lowest point of the swing?",
    "options": ["3mg", "mg", "2mg", "4mg"],
    "answer": 0,
    "explanation": "Conservation of energy from release (height L) to bottom: mgL = (1/2)mv^2 → v^2 = 2gL. At the lowest point, centripetal force equation is T - mg = mv^2 / L. Substitute v^2: T - mg = m(2gL)/L = 2mg → T = 3mg.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.3 Energy and Circular Motion"
  },
  {
    "id": "ap-phys-058",
    "type": "mcq",
    "subtopic": "Spring Launch Velocity (Unit 4)",
    "difficulty": "Medium",
    "question": "A 0.5 kg ball is compressed against a horizontal spring (k = 200 N/m) by 0.2 m on a frictionless tabletop. When released, what is the speed of the ball as it leaves the spring?",
    "options": ["4.0 m/s", "2.0 m/s", "8.0 m/s", "1.41 m/s"],
    "answer": 0,
    "explanation": "Conservation of energy: (1/2)kx^2 = (1/2)mv^2 → kx^2 = mv^2 → v = x * √(k / m) = 0.2 m * √(200 N/m / 0.5 kg) = 0.2 * √400 = 0.2 * 20 = 4.0 m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.3 Conservation of Energy"
  },
  {
    "id": "ap-phys-059",
    "type": "mcq",
    "subtopic": "Centripetal Force Source on Conical Pendulum (Unit 3)",
    "difficulty": "Hard",
    "question": "A conical pendulum of length L and mass m sweeps out a horizontal circle at angle θ with the vertical. What provides the centripetal force keeping the mass in horizontal circular motion?",
    "options": [
      "The horizontal component of the string tension, T * sin(θ)",
      "The vertical component of the string tension, T * cos(θ)",
      "The gravitational force, mg",
      "The centrifugal force acting outward"
    ],
    "answer": 0,
    "explanation": "The string tension T has a vertical component T*cos(θ) which balances gravity mg, and a horizontal component T*sin(θ) pointing toward the center of the circular orbit, which provides the centripetal force (T*sin(θ) = m*v^2 / r).",
    "citation": "College Board AP® Physics 1 CED — Topic 3.2 Circular Motion Dynamics"
  },
  {
    "id": "ap-phys-060",
    "type": "mcq",
    "subtopic": "Power Required to Double Vehicle Speed (Unit 4)",
    "difficulty": "Hard",
    "question": "A car cruises at constant speed v against aerodynamic drag force F_drag = c*v^2. If the driver doubles the cruising speed to 2v, by what factor must the engine power output increase?",
    "options": ["8", "4", "2", "16"],
    "answer": 0,
    "explanation": "Power P = F * v. With aerodynamic drag F = c*v^2, power required is P = (c*v^2) * v = c*v^3. If velocity is doubled (2v), power required becomes c*(2v)^3 = 8 * c*v^3, requiring an 8-fold increase in power.",
    "citation": "College Board AP® Physics 1 CED — Topic 4.4 Power and Velocity Dependencies"
  }
]

# Write AP Physics Set 3
with open(os.path.join(US_DATA_AP, "ap_physics_1_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ap_phys_set3}, f, indent=2, ensure_ascii=False)
print("Generated ap_physics_1_set3.json (20 Qs)!")
