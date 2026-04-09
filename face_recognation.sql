-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 29, 2025 at 10:25 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognation`
--

-- --------------------------------------------------------

--
-- Table structure for table `face_recognizer`
--

CREATE TABLE `face_recognizer` (
  `Student_ID` int(20) NOT NULL,
  `Student_Name` varchar(100) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Course` varchar(100) NOT NULL,
  `Year` int(20) NOT NULL,
  `Semester` varchar(20) NOT NULL,
  `Class_Section` varchar(20) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Blood_Group` varchar(20) NOT NULL,
  `Nationality` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Phone_No` int(20) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Teacher_Name` varchar(100) NOT NULL,
  `Photo_Sample` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `face_recognizer`
--

INSERT INTO `face_recognizer` (`Student_ID`, `Student_Name`, `Department`, `Course`, `Year`, `Semester`, `Class_Section`, `Gender`, `Blood_Group`, `Nationality`, `Email`, `Phone_No`, `Address`, `Teacher_Name`, `Photo_Sample`) VALUES
(123456, 'abc', 'CSE', 'Math', 2022, '4th', 'A', 'Female', 'B+', 'Bangladeshi', 'abc@gmail.com', 14567689, 'Rajshahi', 'SGH', 'Yes'),
(456789, 'sdfghj', 'Pharmacy', 'Data Structures', 2024, '3rd', 'c', 'Male', 'b+', 'dfghjk', 'sdfgbnm', 3456789, 'dfghj', 'sal', 'No'),
(22131108, 'Marufa Mou', 'CSE', 'Math', 2023, '5th', 'C', 'Female', 'A+', 'Bangladeshi', 'marufs@gmail.com', 1987766656, 'Chapai er meye ', 'Salma Akter Limap', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `face_recognizer`
--
ALTER TABLE `face_recognizer`
  ADD PRIMARY KEY (`Student_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `face_recognizer`
--
ALTER TABLE `face_recognizer`
  MODIFY `Student_ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=221311089;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
