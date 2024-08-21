# Postmortem: QTM - Quality Time Management Outage

## Issue Summary
**Duration**:  
- **Start Time**: August 15, 2024, 10:30 AM UTC  
- **End Time**: August 15, 2024, 12:00 PM UTC  
- **Total Duration**: 1 hour 30 minutes

**Impact**:  
During the outage, the QTM - Quality Time Management app experienced a significant slowdown, affecting approximately 60% of users. Users were unable to load their task dashboards, and performance summaries were not generating. New tasks could not be saved, leading to frustration and productivity loss for users during the affected period.

**Root Cause**:  
The root cause of the outage was an unoptimized database query that caused the MySQL database to become overwhelmed, resulting in significant delays in processing requests.

## Timeline
- **10:35 AM** - Issue detected via Datadog alert indicating high response times and increased error rates.
- **10:40 AM** - Engineers started investigating the app server's load and suspected a surge in user activity.
- **10:50 AM** - Backend logs were examined, leading to an assumption that the issue was with the application server.
- **11:00 AM** - Misleading investigation path: Engineers restarted the application servers, assuming a memory leak was causing the issue, but this had no effect.
- **11:15 AM** - Issue escalated to the database team after ruling out the application server as the source of the problem.
- **11:30 AM** - The database team identified a problematic SQL query that was consuming excessive resources.
- **11:40 AM** - Query optimization began by creating an index on the table that was being queried inefficiently.
- **12:00 PM** - The optimized query was deployed, and system performance returned to normal, resolving the outage.

## Root Cause and Resolution
**Root Cause**:  
The outage was caused by an inefficient SQL query within the QTM app that was executed frequently to generate performance summaries. This query lacked proper indexing, resulting in full table scans on a large dataset. As user activity spiked, the database struggled to keep up with the query load, leading to high response times and eventual system slowdown.

**Resolution**:  
The issue was resolved by identifying the problematic query and adding an appropriate index to the database table. This optimization reduced the query's execution time from several seconds to milliseconds, restoring normal application performance. After the fix was deployed, the database load normalized, and the app's responsiveness returned to acceptable levels.

## Corrective and Preventative Measures
**Improvements and Fixes**:
- **Database Optimization**: Review and optimize all database queries, especially those that are executed frequently or operate on large datasets.
- **Index Monitoring**: Implement monitoring for slow queries in MySQL to detect and address similar issues proactively.
- **Load Testing**: Conduct regular load testing to ensure the app can handle peak user activity without performance degradation.
- **Incident Response Training**: Improve incident response by training engineers on effective debugging practices and ensuring familiarity with database performance tuning.

**TODO List**:
1. **Patch**: Update the MySQL server to the latest version for improved performance and security.
2. **Add Monitoring**: Implement query performance monitoring in Datadog to alert on slow queries.
3. **Review Queries**: Audit existing database queries for optimization opportunities.
4. **Implement Load Testing**: Schedule quarterly load tests to simulate high user activity.
5. **Train Team**: Conduct a training session on database indexing and performance optimization techniques.

By addressing these corrective measures, we aim to prevent similar outages in the future and ensure a smoother, more reliable experience for QTM users.
