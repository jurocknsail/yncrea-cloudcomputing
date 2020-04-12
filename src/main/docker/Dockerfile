FROM java:8
EXPOSE 8383
ARG WAR_FILE=target/*.jar
COPY ${WAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]