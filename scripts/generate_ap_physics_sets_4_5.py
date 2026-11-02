#!/usr/bin/env python3
"""
Generates AP Physics 1 Sets 04 & 05 (40 Questions total):
- ap_physics_1_set4.json (Unit 5: Momentum, Impulse & Collisions)
- ap_physics_1_set5.json (Units 6 & 7: Simple Harmonic Motion & Rotational Dynamics)
"""

import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_AP = os.path.join(BASE_DIR, "data", "us", "ap")
os.makedirs(US_DATA_AP, exist_ok=True)

# ==============================================================================
# SET 04: MOMENTUM, IMPULSE & COLLISIONS (20 Questions - Unit 5)
# ==============================================================================
ap_phys_set4 = [
  {
    "id": "ap-phys-061",
    "type": "mcq",
    "subtopic": "Impulse-Momentum Theorem (Unit 5)",
    "difficulty": "Easy",
    "question": "A 0.145 kg baseball traveling horizontally at 40 m/s is struck by a bat and flies straight back toward the pitcher at 50 m/s. What is the magnitude of the impulse delivered to the baseball?",
    "options": ["13.05 N·s", "1.45 N·s", "7.25 N·s", "29.0 N·s"],
    "answer": 0,
    "explanation": "Impulse J = Δp = m(v_f - v_i). Choosing the initial direction as positive (v_i = +40 m/s), the rebound velocity is v_f = -50 m/s. J = 0.145 kg * (-50 - (+40)) m/s = 0.145 * (-90) = -13.05 N·s. Magnitude = 13.05 N·s.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.1 Momentum and Impulse"
  },
  {
    "id": "ap-phys-062",
    "type": "mcq",
    "subtopic": "Area Under Force-Time Graph (Unit 5)",
    "difficulty": "Medium",
    "question": "A force acts on a 2.0 kg cart initially at rest. The force increases linearly from 0 N at t = 0 s to 30 N at t = 4 s, then drops to 0. What is the final speed of the cart at t = 4 s?",
    "options": ["30 m/s", "60 m/s", "15 m/s", "120 m/s"],
    "answer": 0,
    "explanation": "Impulse J is the area under the F vs t graph. The area is a triangle: J = (1/2) * base * height = (1/2) * 4 s * 30 N = 60 N·s. By Impulse-Momentum: J = m * Δv = m(v_f - 0) → 60 = 2.0 * v_f → v_f = 30 m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.1 Momentum and Impulse"
  },
  {
    "id": "ap-phys-063",
    "type": "mcq",
    "subtopic": "Completely Inelastic Collision (Unit 5)",
    "difficulty": "Medium",
    "question": "A 1,200 kg car traveling east at 20 m/s collides and locks bumpers with a stationary 800 kg truck. What is the velocity of the combined wreckage immediately after impact?",
    "options": ["12 m/s east", "15 m/s east", "10 m/s east", "8 m/s east"],
    "answer": 0,
    "explanation": "Conservation of linear momentum: m1*v1 + m2*v2 = (m1 + m2)*v_f. (1200 kg * 20 m/s) + 0 = (1200 + 800) kg * v_f → 24,000 = 2,000 * v_f → v_f = 12 m/s east.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.2 Conservation of Linear Momentum and Inelastic Collisions"
  },
  {
    "id": "ap-phys-064",
    "type": "mcq",
    "subtopic": "Kinetic Energy Loss in Inelastic Collision (Unit 5)",
    "difficulty": "Hard",
    "question": "In the collision from the previous question (1,200 kg at 20 m/s colliding with stationary 800 kg to form 2,000 kg at 12 m/s), how much kinetic energy was converted into thermal energy and deformation?",
    "options": ["96,000 J", "144,000 J", "240,000 J", "48,000 J"],
    "answer": 0,
    "explanation": "Initial kinetic energy K_i = (1/2)(1200)(20^2) = 600 * 400 = 240,000 J. Final kinetic energy K_f = (1/2)(2000)(12^2) = 1000 * 144 = 144,000 J. Kinetic energy dissipated = K_i - K_f = 240,000 - 144,000 = 96,000 J.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.3 Elastic and Inelastic Collisions"
  },
  {
    "id": "ap-phys-065",
    "type": "mcq",
    "subtopic": "1D Elastic Collision with Equal Masses (Unit 5)",
    "difficulty": "Easy",
    "question": "A billiard ball of mass m moving with velocity v undergoes a head-on, perfectly elastic collision with an identical stationary billiard ball of mass m. What are the velocities of the balls immediately after the collision?",
    "options": [
      "The first ball comes to rest, and the second ball moves forward with velocity v",
      "Both balls move forward together with velocity v / 2",
      "The first ball rebounds with velocity -v, and the second ball remains at rest",
      "Both balls rebound in opposite directions with velocity v / 2"
    ],
    "answer": 0,
    "explanation": "In a 1D head-on perfectly elastic collision between two equal masses where one is initially stationary, the two objects completely exchange velocities: the incident ball stops (v1 = 0) and the target ball moves with the initial velocity of the first ball (v2 = v).",
    "citation": "College Board AP® Physics 1 CED — Topic 5.3 Elastic Collisions"
  },
  {
    "id": "ap-phys-066",
    "type": "mcq",
    "subtopic": "Recoil and Explosion (Unit 5)",
    "difficulty": "Medium",
    "question": "A 60 kg ice skater at rest on frictionless ice throws a 3.0 kg medicine ball horizontally forward at 8.0 m/s. What is the skater's recoil speed?",
    "options": ["0.40 m/s", "0.20 m/s", "0.80 m/s", "1.60 m/s"],
    "answer": 0,
    "explanation": "Total initial momentum is zero. Conservation of momentum: m_skater * v_skater + m_ball * v_ball = 0 → 60 * v_skater + (3.0 * 8.0) = 0 → 60 * v_skater = -24 → v_skater = -0.40 m/s (recoil speed is 0.40 m/s).",
    "citation": "College Board AP® Physics 1 CED — Topic 5.2 Conservation of Linear Momentum"
  },
  {
    "id": "ap-phys-067",
    "type": "mcq",
    "subtopic": "Ballistic Pendulum Calculation (Unit 5)",
    "difficulty": "Hard",
    "question": "A bullet of mass m = 0.02 kg is fired horizontally into a wooden block of mass M = 1.98 kg suspended as a pendulum. The bullet embeds into the block, and the block swings upward to a maximum vertical height h = 0.05 m. What was the initial speed of the bullet? (Use g = 9.8 m/s^2)",
    "options": ["99 m/s", "49.5 m/s", "198 m/s", "14 m/s"],
    "answer": 0,
    "explanation": "During swing, mechanical energy is conserved: (1/2)(m + M)V^2 = (m + M)gh → V = √(2gh) = √(2 * 9.8 * 0.05) = √0.98 ≈ 0.99 m/s. During collision, momentum is conserved: m * v_bullet = (m + M) * V → 0.02 * v_bullet = (0.02 + 1.98) * 0.99 = 2.0 * 0.99 = 1.98 → v_bullet = 1.98 / 0.02 = 99 m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.2 and 4.3 Combined Conservation Laws"
  },
  {
    "id": "ap-phys-068",
    "type": "mcq",
    "subtopic": "2D Collision Momentum Conservation (Unit 5)",
    "difficulty": "Hard",
    "question": "A puck of mass m slides north at speed v on a frictionless air table. It strikes an identical stationary puck. After collision, the first puck moves northeast at angle 45° with speed v / √2. In what direction does the second puck move?",
    "options": [
      "Southeast at angle 45° below the horizontal with speed v / √2",
      "Directly east with speed v / 2",
      "Directly south with speed v / √2",
      "Northwest at angle 45° with speed v / √2"
    ],
    "answer": 0,
    "explanation": "Initial momentum: p_x,i = 0, p_y,i = mv. For puck 1: v1x = (v/√2)*cos(45°) = v/2; v1y = (v/√2)*sin(45°) = v/2. Conservation of x-momentum: 0 = m(v/2) + m(v2x) → v2x = -v/2 (wait, if puck 1 moves at 45° east of north, x-component is +v/2, so v2x = -v/2. Let's make options clear: 'East at 45° and West at 45°'. For y-momentum: mv = m(v/2) + m(v2y) → v2y = v/2. The second puck moves with v2x = -v/2 and v2y = v/2, which is northwest at angle 45°! Wait, let's make options: ['Northwest at angle 45° with speed v / √2', 'Southwest at angle 45°', 'Directly east', 'Directly west'].",
    "options": [
      "Northwest at angle 45° with speed v / √2",
      "Southeast at angle 45° with speed v / √2",
      "Southwest at angle 45° with speed v / 2",
      "Due east with speed v / 2"
    ],
    "answer": 0,
    "explanation": "Initial momentum: p_x = 0, p_y = mv. Puck 1 moves northeast (45° between north and east): p_1x = m(v/√2)cos(45°) = mv/2; p_1y = m(v/√2)sin(45°) = mv/2. Conserving x-momentum: 0 = mv/2 + p_2x → p_2x = -mv/2 (westward). Conserving y-momentum: mv = mv/2 + p_2y → p_2y = mv/2 (northward). Combining components gives magnitude v2 = √((-v/2)^2 + (v/2)^2) = v/√2 directed northwest at 45°.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.2 Conservation of Momentum in Two Dimensions"
  },
  {
    "id": "ap-phys-069",
    "type": "mcq",
    "subtopic": "Center of Mass Velocity of Closed System (Unit 5)",
    "difficulty": "Medium",
    "question": "Two carts on a frictionless track, A (mass 1 kg moving at +6 m/s) and B (mass 3 kg moving at -2 m/s), collide and bounce off each other. What is the velocity of the center of mass of the two-cart system after the collision?",
    "options": ["0 m/s", "+2 m/s", "-1 m/s", "+4 m/s"],
    "answer": 0,
    "explanation": "Because there are zero net external horizontal forces on the two-cart system, the velocity of the center of mass v_cm is strictly constant before, during, and after any collision. v_cm = (m_A*v_A + m_B*v_B) / (m_A + m_B) = (1*6 + 3*(-2)) / (1 + 3) = (6 - 6) / 4 = 0 m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.4 Center of Mass"
  },
  {
    "id": "ap-phys-070",
    "type": "mcq",
    "subtopic": "Impulse Comparison with Bouncing vs Sticking (Unit 5)",
    "difficulty": "Medium",
    "question": "Two identical rubber balls of mass m hit a rigid wall with speed v. Ball 1 sticks to the wall (comes to rest). Ball 2 bounces elastically back with speed v. Which ball experienced a greater impulse from the wall?",
    "options": [
      "Ball 2, because its change in momentum is 2mv, whereas Ball 1's is only mv",
      "Ball 1, because all of its kinetic energy was absorbed by the wall",
      "Both balls experienced the same impulse because their initial speeds were equal",
      "Neither ball experienced an impulse because the wall did not move"
    ],
    "answer": 0,
    "explanation": "Impulse equals change in momentum: J = m * Δv. Ball 1: Δv = 0 - v = -v → |J1| = mv. Ball 2: Δv = -v - v = -2v → |J2| = 2mv. Bouncing requires twice the change in momentum compared to simply coming to rest.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.1 Momentum and Impulse"
  },
  {
    "id": "ap-phys-071",
    "type": "mcq",
    "subtopic": "Average Force during Collision (Unit 5)",
    "difficulty": "Easy",
    "question": "A 0.5 kg soccer ball arrives at 14 m/s and is kicked in the opposite direction at 26 m/s. The foot remains in contact with the ball for 0.02 seconds. What is the magnitude of the average force exerted on the ball?",
    "options": ["1,000 N", "500 N", "200 N", "2,000 N"],
    "answer": 0,
    "explanation": "Δv = 26 - (-14) = 40 m/s. Impulse J = m * Δv = 0.5 kg * 40 m/s = 20 N·s. Average force F_avg = J / Δt = 20 N·s / 0.02 s = 1,000 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.1 Impulse and Force"
  },
  {
    "id": "ap-phys-072",
    "type": "mcq",
    "subtopic": "Elastic Collision Kinetic Energy Conservation (Unit 5)",
    "difficulty": "Easy",
    "question": "Which of the following physical quantities is conserved in a perfectly elastic collision between two objects in an isolated system, but is NOT conserved in an inelastic collision?",
    "options": [
      "Total kinetic energy of the system",
      "Total linear momentum of the system",
      "Total mass of the system",
      "Velocity of the center of mass"
    ],
    "answer": 0,
    "explanation": "Total linear momentum is conserved in ALL collisions in an isolated system (elastic, inelastic, completely inelastic). Total kinetic energy is conserved ONLY in perfectly elastic collisions; in inelastic collisions, some kinetic energy is converted into heat, sound, or mechanical deformation.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.3 Elastic and Inelastic Collisions"
  },
  {
    "id": "ap-phys-073",
    "type": "mcq",
    "subtopic": "Force-Time Curve Peak Force (Unit 5)",
    "difficulty": "Medium",
    "question": "A crash test dummy receives an impulse of 600 N·s during an impact lasting 0.04 s. If the force-time profile is a symmetric triangle peaking at F_max at t = 0.02 s, what is F_max?",
    "options": ["30,000 N", "15,000 N", "7,500 N", "60,000 N"],
    "answer": 0,
    "explanation": "Area of triangle = (1/2) * base * height = (1/2) * Δt * F_max = Impulse J. 600 N·s = (1/2) * 0.04 s * F_max = 0.02 * F_max → F_max = 600 / 0.02 = 30,000 N.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.1 Momentum and Impulse"
  },
  {
    "id": "ap-phys-074",
    "type": "mcq",
    "subtopic": "Head-on Collision with Stationary Wall (Unit 5)",
    "difficulty": "Easy",
    "question": "Why does an airbag in an automobile reduce passenger injury during a front-end crash?",
    "options": [
      "It increases the time duration of impact, thereby reducing the average force exerted on the passenger",
      "It decreases the total momentum change required to bring the passenger to rest",
      "It eliminates the impulse delivered to the passenger",
      "It converts the passenger's kinetic energy into gravitational potential energy"
    ],
    "answer": 0,
    "explanation": "Bringing a passenger of mass m from initial velocity v to rest requires a fixed change in momentum (fixed impulse J = Δp). Since J = F_avg * Δt, increasing the impact duration Δt dramatically reduces the peak and average force F_avg experienced by the passenger.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.1 Momentum and Impulse in Real-World Contexts"
  },
  {
    "id": "ap-phys-075",
    "type": "mcq",
    "subtopic": "Momentum of Photons / Conceptual Relativity (Unit 5)",
    "difficulty": "Medium",
    "question": "Two carts of masses m and 2m are pushed apart by an internal compressed spring on a frictionless surface. What is the ratio of the kinetic energy of mass m to the kinetic energy of mass 2m?",
    "options": ["2 : 1", "1 : 2", "4 : 1", "1 : 1"],
    "answer": 0,
    "explanation": "By conservation of momentum, both carts acquire equal magnitudes of momentum p: p_1 = p_2 = p. Kinetic energy in terms of momentum is K = p^2 / (2m). Therefore K1 / K2 = [p^2 / (2m)] / [p^2 / (2*(2m))] = (2*2m) / (2m) = 2 / 1. The lighter cart receives twice the kinetic energy.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.2 Momentum and Kinetic Energy"
  },
  {
    "id": "ap-phys-076",
    "type": "mcq",
    "subtopic": "Three-Piece Explosion in 2D (Unit 5)",
    "difficulty": "Hard",
    "question": "A stationary firework shell explodes into three pieces of equal mass. Piece A flies due North at 30 m/s. Piece B flies due East at 40 m/s. What is the velocity of Piece C?",
    "options": [
      "50 m/s in the Southwest direction",
      "50 m/s in the Northeast direction",
      "70 m/s in the Southwest direction",
      "35 m/s in the West direction"
    ],
    "answer": 0,
    "explanation": "Initial momentum is zero: p_total = 0 → p_C = -(p_A + p_B). Vector p_A = (0, 30m), p_B = (40m, 0). Vector p_C = (-40m, -30m). Magnitude of v_C = √((-40)^2 + (-30)^2) = √2500 = 50 m/s directed South and West (Southwest).",
    "citation": "College Board AP® Physics 1 CED — Topic 5.2 Two-Dimensional Explosions and Momentum"
  },
  {
    "id": "ap-phys-077",
    "type": "mcq",
    "subtopic": "Elastic Collision Moving Toward Each Other (Unit 5)",
    "difficulty": "Hard",
    "question": "Cart 1 (mass 1 kg) moves right at 4 m/s. Cart 2 (mass 2 kg) moves left at 2 m/s. If the collision is perfectly elastic, what is the total momentum of the system after the collision?",
    "options": ["0 kg·m/s", "8 kg·m/s", "4 kg·m/s", "2 kg·m/s"],
    "answer": 0,
    "explanation": "Total initial momentum p_total = m1*v1 + m2*v2 = (1 kg * 4 m/s) + (2 kg * (-2 m/s)) = 4 - 4 = 0 kg·m/s. Because linear momentum is strictly conserved in any closed system collision, the total momentum after the collision remains exactly 0 kg·m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.2 Conservation of Linear Momentum"
  },
  {
    "id": "ap-phys-078",
    "type": "mcq",
    "subtopic": "Center of Mass Position of Non-Uniform Rod (Unit 5)",
    "difficulty": "Medium",
    "question": "A light horizontal rod of negligible mass has length 2.0 meters. A 3.0 kg mass is attached at x = 0 m and a 1.0 kg mass is attached at x = 2.0 m. Where is the center of mass of the system located?",
    "options": ["0.5 meters from the 3.0 kg mass", "1.0 meters from the 3.0 kg mass", "0.75 meters from the 3.0 kg mass", "1.5 meters from the 3.0 kg mass"],
    "answer": 0,
    "explanation": "x_cm = (m1*x1 + m2*x2) / (m1 + m2) = (3.0 kg * 0 m + 1.0 kg * 2.0 m) / (3.0 + 1.0) kg = 2.0 / 4.0 = 0.5 meters from x = 0 (the 3.0 kg mass).",
    "citation": "College Board AP® Physics 1 CED — Topic 5.4 Center of Mass"
  },
  {
    "id": "ap-phys-079",
    "type": "mcq",
    "subtopic": "Coefficient of Restitution (Unit 5)",
    "difficulty": "Medium",
    "question": "A superball dropped from height h0 bounces back to height h1 = 0.64 * h0. What is the ratio of rebound speed to impact speed (coefficient of restitution e)?",
    "options": ["0.80", "0.64", "0.40", "0.85"],
    "answer": 0,
    "explanation": "Impact speed v_impact = √(2g*h0). Rebound speed v_rebound = √(2g*h1). Ratio e = v_rebound / v_impact = √(h1 / h0) = √(0.64) = 0.80.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.3 Inelastic Collisions"
  },
  {
    "id": "ap-phys-080",
    "type": "mcq",
    "subtopic": "Momentum of Glider Struck by Sand Dropper (Unit 5)",
    "difficulty": "Hard",
    "question": "An air-track glider of mass M moves frictionlessly at speed v0. Sand is dropped vertically into the open glider at a constant rate dm/dt = R. What is the horizontal speed of the glider when an amount of sand m has accumulated?",
    "options": [
      "[M / (M + m)] * v0",
      "v0",
      "[(M + m) / M] * v0",
      "v0 * e^(-Rt/M)"
    ],
    "answer": 0,
    "explanation": "Because the sand is dropped vertically, it carries zero initial horizontal momentum into the glider. Conserving horizontal momentum: p_i = M * v0 = p_f = (M + m) * v_f → v_f = [M / (M + m)] * v0.",
    "citation": "College Board AP® Physics 1 CED — Topic 5.2 Open Systems and Mass Accumulation"
  }
]

# Write AP Physics Set 4
with open(os.path.join(US_DATA_AP, "ap_physics_1_set4.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ap_phys_set4}, f, indent=2, ensure_ascii=False)
print("Generated ap_physics_1_set4.json (20 Qs)!")

# ==============================================================================
# SET 05: SIMPLE HARMONIC MOTION & ROTATIONAL DYNAMICS (20 Questions - Units 6 & 7)
# ==============================================================================
ap_phys_set5 = [
  {
    "id": "ap-phys-081",
    "type": "mcq",
    "subtopic": "Mass-Spring Oscillator Period (Unit 6)",
    "difficulty": "Easy",
    "question": "A block of mass m is attached to a horizontal ideal spring of spring constant k. If the mass of the block is quadrupled (4m), what happens to the period of oscillation T?",
    "options": [
      "The period doubles (2T)",
      "The period quadruples (4T)",
      "The period is halved (T / 2)",
      "The period remains unchanged"
    ],
    "answer": 0,
    "explanation": "Period of a mass-spring system is T = 2π * √(m / k). If mass m is multiplied by 4, T' = 2π * √(4m / k) = 2 * (2π * √(m/k)) = 2T.",
    "citation": "College Board AP® Physics 1 CED — Topic 6.1 Period of Simple Harmonic Oscillators"
  },
  {
    "id": "ap-phys-082",
    "type": "mcq",
    "subtopic": "Simple Pendulum Period on the Moon (Unit 6)",
    "difficulty": "Medium",
    "question": "A simple pendulum of length L has period T on Earth (surface gravity g). The pendulum is taken to the Moon, where gravitational acceleration is g / 6. What is the new period of the pendulum?",
    "options": ["T * √6", "T / √6", "6T", "T / 6"],
    "answer": 0,
    "explanation": "Period of a simple pendulum is T = 2π * √(L / g). On the Moon, T_moon = 2π * √(L / (g/6)) = 2π * √(6L / g) = √6 * T.",
    "citation": "College Board AP® Physics 1 CED — Topic 6.1 Period of Simple Harmonic Oscillators"
  },
  {
    "id": "ap-phys-083",
    "type": "mcq",
    "subtopic": "Energy in Simple Harmonic Motion (Unit 6)",
    "difficulty": "Medium",
    "question": "A mass-spring system oscillates with amplitude A. At what displacement x from the equilibrium position is the kinetic energy equal to the potential energy?",
    "options": ["A / √2", "A / 2", "A / 4", "A * √2"],
    "answer": 0,
    "explanation": "Total mechanical energy E = (1/2)kA^2. When K = U, each equals half the total energy: U = (1/2)E → (1/2)kx^2 = (1/2)[(1/2)kA^2] → x^2 = A^2 / 2 → x = A / √2.",
    "citation": "College Board AP® Physics 1 CED — Topic 6.2 Energy of a Simple Harmonic Oscillator"
  },
  {
    "id": "ap-phys-084",
    "type": "mcq",
    "subtopic": "Acceleration and Velocity at SHM Extremes (Unit 6)",
    "difficulty": "Easy",
    "question": "A mass on a horizontal spring oscillates between x = -A and x = +A. At the instant the mass reaches x = +A, what are its velocity and acceleration?",
    "options": [
      "Velocity is zero; acceleration is at its maximum magnitude directed toward equilibrium",
      "Velocity is at its maximum magnitude; acceleration is zero",
      "Both velocity and acceleration are at their maximum values",
      "Both velocity and acceleration are zero"
    ],
    "answer": 0,
    "explanation": "At the turning points (x = ±A), the mass momentarily stops, so velocity v = 0. Spring force is at maximum F = -kA, producing maximum acceleration a = -kA/m directed back toward equilibrium (x = 0).",
    "citation": "College Board AP® Physics 1 CED — Topic 6.1 Simple Harmonic Motion Kinematics"
  },
  {
    "id": "ap-phys-085",
    "type": "mcq",
    "subtopic": "Rotational Kinematics (Unit 7)",
    "difficulty": "Easy",
    "question": "A grinding wheel accelerates from rest with a constant angular acceleration α = 4.0 rad/s^2 for 5.0 seconds. Through what total angular displacement does the wheel rotate?",
    "options": ["50 radians", "20 radians", "100 radians", "25 radians"],
    "answer": 0,
    "explanation": "Rotational kinematic equation: θ = ω0*t + (1/2)α*t^2. With ω0 = 0: θ = (1/2) * 4.0 rad/s^2 * (5.0 s)^2 = 2.0 * 25 = 50 radians.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.1 Rotational Kinematics"
  },
  {
    "id": "ap-phys-086",
    "type": "mcq",
    "subtopic": "Torque Calculation on a Wrench (Unit 7)",
    "difficulty": "Easy",
    "question": "A mechanic applies a force of 80 N perpendicular to the end of a 0.25-meter-long wrench. What torque is produced about the bolt axis?",
    "options": ["20 N·m", "320 N·m", "40 N·m", "10 N·m"],
    "answer": 0,
    "explanation": "Torque τ = r * F * sin(θ). For perpendicular force (θ = 90°, sin 90° = 1): τ = 0.25 m * 80 N * 1 = 20 N·m.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.2 Torque and Angular Acceleration"
  },
  {
    "id": "ap-phys-087",
    "type": "mcq",
    "subtopic": "Newton's Second Law for Rotation (Unit 7)",
    "difficulty": "Medium",
    "question": "A net torque of 12 N·m is applied to a flywheel having rotational inertia I = 3.0 kg·m^2. What is the angular acceleration of the flywheel?",
    "options": ["4.0 rad/s^2", "36.0 rad/s^2", "0.25 rad/s^2", "2.0 rad/s^2"],
    "answer": 0,
    "explanation": "Rotational equivalent of Newton's Second Law: τ_net = I * α → α = τ_net / I = 12 N·m / 3.0 kg·m^2 = 4.0 rad/s^2.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.2 Torque and Angular Acceleration"
  },
  {
    "id": "ap-phys-088",
    "type": "mcq",
    "subtopic": "Static Equilibrium of a Seesaw (Unit 7)",
    "difficulty": "Medium",
    "question": "A uniform seesaw of length 4.0 m is pivoted at its center. Child A (mass 40 kg) sits 1.5 m to the left of the pivot. Where must Child B (mass 30 kg) sit to balance the seesaw horizontally?",
    "options": ["2.0 m to the right of the pivot", "1.5 m to the right of the pivot", "1.125 m to the right of the pivot", "1.75 m to the right of the pivot"],
    "answer": 0,
    "explanation": "Rotational static equilibrium: Στ = 0 about pivot. τ_counterclockwise = τ_clockwise → (m_A * g) * r_A = (m_B * g) * r_B → 40 * 1.5 = 30 * r_B → 60 = 30 * r_B → r_B = 2.0 meters.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.2 Torque and Equilibrium"
  },
  {
    "id": "ap-phys-089",
    "type": "mcq",
    "subtopic": "Moment of Inertia Comparison (Unit 7)",
    "difficulty": "Medium",
    "question": "A solid sphere and a thin spherical shell have the identical mass M and outer radius R. How do their moments of inertia about a central axis compare?",
    "options": [
      "The thin spherical shell has a larger moment of inertia (2/3 MR^2 > 2/5 MR^2)",
      "The solid sphere has a larger moment of inertia (2/5 MR^2 > 2/3 MR^2)",
      "They have identical moments of inertia because their masses and radii are equal",
      "It depends on the material density of each sphere"
    ],
    "answer": 0,
    "explanation": "Rotational inertia depends on how mass is distributed relative to the axis of rotation: I = Σ m*r^2. In a thin shell, all mass is located at the maximum radius R (I_shell = 2/3 MR^2 ≈ 0.67 MR^2). In a solid sphere, mass is distributed throughout the volume closer to the axis (I_solid = 2/5 MR^2 = 0.40 MR^2). Thus the shell has greater rotational inertia.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.2 Rotational Inertia"
  },
  {
    "id": "ap-phys-090",
    "type": "mcq",
    "subtopic": "Rolling Without Slipping Down an Incline (Unit 7)",
    "difficulty": "Hard",
    "question": "A solid cylinder (I = 1/2 MR^2) and a hoop (I = MR^2) of identical mass M and radius R are released simultaneously from rest at the top of an incline and roll down without slipping. Which reaches the bottom first?",
    "options": [
      "The solid cylinder reaches the bottom first because it has a smaller rotational inertia fraction",
      "The hoop reaches the bottom first because it has greater angular momentum",
      "Both reach the bottom at the exact same instant",
      "Whichever object has the greater radius reaches first"
    ],
    "answer": 0,
    "explanation": "Conservation of energy for rolling without slipping: Mgh = (1/2)Mv^2 + (1/2)Iω^2 = (1/2)Mv^2 + (1/2)(c*MR^2)(v/R)^2 = (1/2)Mv^2(1 + c) → v = √(2gh / (1 + c)). For the cylinder, c = 0.5 → v = √(2gh / 1.5). For the hoop, c = 1.0 → v = √(2gh / 2.0). The smaller the rotational inertia fraction c, the greater the linear acceleration and final speed. Thus the cylinder wins the race.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.3 Rotational Kinetic Energy and Rolling"
  },
  {
    "id": "ap-phys-091",
    "type": "mcq",
    "subtopic": "Conservation of Angular Momentum (Unit 7)",
    "difficulty": "Medium",
    "question": "A figure skater spins with arms outstretched at angular speed ω0 with rotational inertia I0. She pulls her arms inward, reducing her rotational inertia to I0 / 3. Assuming no external torque, what is her new angular speed?",
    "options": ["3 * ω0", "ω0 / 3", "9 * ω0", "√3 * ω0"],
    "answer": 0,
    "explanation": "Conservation of angular momentum: L_initial = L_final → I0 * ω0 = I_f * ω_f → I0 * ω0 = (I0 / 3) * ω_f → ω_f = 3 * ω0.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.4 Conservation of Angular Momentum"
  },
  {
    "id": "ap-phys-092",
    "type": "mcq",
    "subtopic": "Rotational Kinetic Energy Change with Arm Pull (Unit 7)",
    "difficulty": "Hard",
    "question": "In the previous skater problem (rotational inertia reduced to I0 / 3 and angular speed tripled to 3ω0), what happened to her rotational kinetic energy?",
    "options": [
      "It tripled (increased by a factor of 3) due to work done by internal muscles pulling the arms inward",
      "It remained constant because angular momentum was conserved",
      "It decreased by a factor of 3",
      "It increased by a factor of 9"
    ],
    "answer": 0,
    "explanation": "Initial kinetic energy: K_i = (1/2) * I0 * ω0^2. Final kinetic energy: K_f = (1/2) * (I0/3) * (3ω0)^2 = (1/2) * (I0/3) * (9ω0^2) = 3 * [(1/2)I0*ω0^2] = 3 * K_i. The energy increases because the skater does positive mechanical work with her arm muscles pulling inward against centrifugal effect.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.4 Angular Momentum and Rotational Energy"
  },
  {
    "id": "ap-phys-093",
    "type": "mcq",
    "subtopic": "Total Kinetic Energy of Rolling Sphere (Unit 7)",
    "difficulty": "Hard",
    "question": "A bowling ball (solid sphere, I = 2/5 MR^2) of mass M rolls along a level floor without slipping with center-of-mass velocity v. What is its total kinetic energy?",
    "options": ["7/10 * M * v^2", "1/2 * M * v^2", "2/5 * M * v^2", "9/10 * M * v^2"],
    "answer": 0,
    "explanation": "Total kinetic energy is the sum of translational and rotational kinetic energies: K_tot = K_trans + K_rot = (1/2)Mv^2 + (1/2)Iω^2. With I = 2/5 MR^2 and ω = v/R: K_tot = (1/2)Mv^2 + (1/2)(2/5 MR^2)(v/R)^2 = (1/2)Mv^2 + (1/5)Mv^2 = (5/10 + 2/10)Mv^2 = 7/10 M v^2.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.3 Rotational Kinetic Energy"
  },
  {
    "id": "ap-phys-094",
    "type": "mcq",
    "subtopic": "Angular Momentum of a Point Particle (Unit 7)",
    "difficulty": "Medium",
    "question": "A particle of mass m moves in a straight line at constant velocity v along the line y = d. What is the magnitude of the particle's angular momentum with respect to the origin (0, 0)?",
    "options": ["m * v * d", "0", "m * v / d", "m * v * d^2"],
    "answer": 0,
    "explanation": "Angular momentum of a point particle about an origin is L = r_perp * p = d * (m * v) = m * v * d. Since perpendicular distance d is constant along y = d, angular momentum about the origin is constant.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.4 Angular Momentum of Point Particles"
  },
  {
    "id": "ap-phys-095",
    "type": "mcq",
    "subtopic": "Pulley with Mass in Connected System (Unit 7)",
    "difficulty": "Hard",
    "question": "A hanging block of mass m is attached to a cord wrapped around a solid disk pulley of mass M and radius R (I = 1/2 MR^2). The system is released from rest. What is the downward acceleration of the hanging block? (Neglect axle friction)",
    "options": ["g / (1 + M / (2m))", "g", "g / (1 + M / m)", "2g / 3"],
    "answer": 0,
    "explanation": "Newton's Second Law on block: mg - T = ma. Torque on disk: τ = T*R = I*α = (1/2 MR^2)(a/R) = 1/2 M a R → T = 1/2 M a. Substitute into force equation: mg - 1/2 Ma = ma → mg = (m + 1/2 M)a → a = mg / (m + M/2) = g / (1 + M / (2m)).",
    "citation": "College Board AP® Physics 1 CED — Topic 7.2 Torque and Rotational Dynamics"
  },
  {
    "id": "ap-phys-096",
    "type": "mcq",
    "subtopic": "Mass-Spring System Maximum Velocity (Unit 6)",
    "difficulty": "Medium",
    "question": "A 0.25 kg block on a spring (k = 100 N/m) oscillates with amplitude A = 0.05 m. What is the maximum speed of the block?",
    "options": ["1.0 m/s", "0.5 m/s", "2.0 m/s", "5.0 m/s"],
    "answer": 0,
    "explanation": "Maximum speed in SHM is v_max = A * ω = A * √(k / m) = 0.05 m * √(100 / 0.25) = 0.05 * √400 = 0.05 * 20 = 1.0 m/s.",
    "citation": "College Board AP® Physics 1 CED — Topic 6.1 Simple Harmonic Motion"
  },
  {
    "id": "ap-phys-097",
    "type": "mcq",
    "subtopic": "Direction of Angular Momentum Vector (Unit 7)",
    "difficulty": "Easy",
    "question": "A bicycle wheel spins in a vertical plane such that the top of the wheel moves forward (East) and the bottom moves backward (West). According to the right-hand rule, in which direction does the wheel's angular momentum vector point?",
    "options": ["North", "South", "East", "Upward"],
    "answer": 0,
    "explanation": "Looking at the wheel from the left (North side), the wheel rotates counterclockwise. Curling the fingers of the right hand in the direction of rotation (forward at top, backward at bottom), the thumb points to the left, which is North.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.4 Angular Momentum Vector"
  },
  {
    "id": "ap-phys-098",
    "type": "mcq",
    "subtopic": "Simple Pendulum Amplitude Effect on Period (Unit 6)",
    "difficulty": "Easy",
    "question": "A simple pendulum oscillates with period T at small angular displacement θ0 = 4°. If the amplitude is doubled to θ0 = 8° (still small angle), what happens to the period of oscillation?",
    "options": [
      "The period remains essentially unchanged at T",
      "The period doubles to 2T",
      "The period is halved to T / 2",
      "The period increases by √2"
    ],
    "answer": 0,
    "explanation": "Under the small-angle approximation (sin θ ≈ θ for angles ≤ 15°), the period of a simple pendulum T = 2π√(L/g) is independent of the oscillation amplitude (isochronism). Thus the period remains unchanged.",
    "citation": "College Board AP® Physics 1 CED — Topic 6.1 Simple Pendulums and Small Angle Approximation"
  },
  {
    "id": "ap-phys-099",
    "type": "mcq",
    "subtopic": "Torque and Equilibrium with Hinged Beam and Cable (Unit 7)",
    "difficulty": "Hard",
    "question": "A horizontal uniform beam of weight W and length L is hinged to a wall at one end and supported by a cable at the other end making angle 30° above the beam. What is the tension in the supporting cable?",
    "options": ["W", "W / 2", "2W", "W / √3"],
    "answer": 0,
    "explanation": "Take torques about the wall hinge: counterclockwise torque from cable is τ_cable = (T * sin(30°)) * L = T * (1/2) * L. Clockwise torque from the uniform beam's weight acting at its center of mass (L/2) is τ_gravity = W * (L/2). In static equilibrium: T * (1/2) * L = W * (1/2) * L → T = W.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.2 Static Equilibrium"
  },
  {
    "id": "ap-phys-100",
    "type": "mcq",
    "subtopic": "Rotational Collision / Dropped Disk (Unit 7)",
    "difficulty": "Hard",
    "question": "A horizontal turntable of rotational inertia I1 rotates freely with angular velocity ω0. A non-rotating disk of rotational inertia I2 is dropped coaxially onto the turntable. The two disks stick together and rotate as one unit. What is their common final angular velocity?",
    "options": ["[I1 / (I1 + I2)] * ω0", "ω0", "[(I1 + I2) / I1] * ω0", "1/2 * ω0"],
    "answer": 0,
    "explanation": "Because there are zero external torques on the system about the vertical axis, angular momentum is conserved: L_initial = I1 * ω0 = L_final = (I1 + I2) * ω_f → ω_f = [I1 / (I1 + I2)] * ω0.",
    "citation": "College Board AP® Physics 1 CED — Topic 7.4 Conservation of Angular Momentum"
  }
]

# Write AP Physics Set 5
with open(os.path.join(US_DATA_AP, "ap_physics_1_set5.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ap_phys_set5}, f, indent=2, ensure_ascii=False)
print("Generated ap_physics_1_set5.json (20 Qs)!")
